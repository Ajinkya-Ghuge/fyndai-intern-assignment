# ----------------------------------------------------------------------
# FYND AI INTERN - TAKE HOME ASSESSMENT - TASK 1
# Rating Prediction via Prompting (Python Notebook)
# ----------------------------------------------------------------------

# 1. Setup and Initialization
# ----------------------------------------------------------------------

# Required libraries: pandas for data, pydantic for structured output schema, 
# google-genai for the LLM API, and sklearn for the accuracy score.


import pandas as pd
import json
import random
import time
from pydantic import BaseModel, Field
from google import genai
from google.genai import types
from google.genai.errors import APIError
from sklearn.metrics import accuracy_score

# --- Configuration ---
API_KEY = "AIzaSyCaNFpCLcxHWVCm82ZO6UmWIqrgwghyW9w"  # <-- PASTE YOUR API KEY HERE
LLM_MODEL = "gemini-2.5-flash"  # Recommended for speed and structured output

if API_KEY == "YOUR_API_KEY":
    raise ValueError("Please replace 'YOUR_API_KEY' with your actual Gemini API key.")

try:
    client = genai.Client(api_key=API_KEY)
except Exception as e:
    print(f"Error initializing Gemini client: {e}")
    # Proceed with data loading and sampling to prepare, but API calls will fail

# Define the required output structure using Pydantic
class ReviewPrediction(BaseModel):
    """Schema for the LLM's required output structure (1-5 star prediction)."""
    predicted_stars: int = Field(..., description="The predicted star rating (1 to 5).")
    explanation: str = Field(..., description="A brief reasoning for the assigned rating.")


# 2. Data Loading and Sampling
# ----------------------------------------------------------------------

FILE_PATH = 'yelp.csv' # User specified file path
SAMPLE_SIZE = 200 # Recommended sample size

try:
    # The Yelp dataset columns usually include 'text' and 'stars'.
    df = pd.read_csv(FILE_PATH) 
    
    # Check for required columns based on common Yelp dataset structures
    if 'text' not in df.columns or 'stars' not in df.columns:
        print("Warning: CSV does not contain expected 'text' and 'stars' columns.")
        # Attempt to use the first two columns if named differently (common in some Kaggle versions)
        if df.columns[0].lower() in ['stars', 'class', 'rating'] and df.columns[1].lower() in ['text', 'review']:
            df = df.rename(columns={df.columns[0]: 'stars', df.columns[1]: 'text'})
        else:
             raise KeyError("Required columns 'text' and 'stars' not found in the CSV.")

except FileNotFoundError:
    raise FileNotFoundError(f"Error: Dataset file '{FILE_PATH}' not found. Please ensure it is in the correct directory.")
except KeyError as e:
    raise KeyError(f"Data loading failed: {e}")
except Exception as e:
    raise Exception(f"An unexpected error occurred during data loading: {e}")

# Sample the data for evaluation
if len(df) > SAMPLE_SIZE:
    df_sample = df.sample(n=SAMPLE_SIZE, random_state=42).reset_index(drop=True)
else:
    df_sample = df.copy()

# Ensure stars are integers for comparison
df_sample['stars'] = df_sample['stars'].astype(int) 

print(f"Dataset loaded and sampled. Evaluation size: {len(df_sample)} rows.")

# Prepare DataFrame to store results for all versions
results_df = df_sample[['text', 'stars']].copy()
results_df.columns = ['review_text', 'actual_stars']


# 3. LLM Call Helper Function
# ----------------------------------------------------------------------

def get_llm_prediction(prompt_template, review_text, model_name=LLM_MODEL, schema=ReviewPrediction):
    """Calls the LLM with a specific prompt and schema for structured JSON output."""
    
    full_prompt = prompt_template.format(review=review_text)

    try:
        response = client.models.generate_content(
            model=model_name,
            contents=[full_prompt],
            config=types.GenerateContentConfig(
                # Enforce JSON output using the Pydantic schema
                response_mime_type="application/json",
                response_schema=schema,
                temperature=0.0 # Low temperature for reliable classification
            )
        )
        
        # The response.text is the guaranteed JSON string
        raw_json_output = response.text
        
        # Validate and parse the JSON string using the Pydantic model
        parsed_output = schema.model_validate_json(raw_json_output)
        
        # Check that the predicted stars is within the valid range (1-5)
        if not (1 <= parsed_output.predicted_stars <= 5):
            return None, f"Predicted stars ({parsed_output.predicted_stars}) is out of range (1-5).", False, raw_json_output

        return parsed_output.predicted_stars, parsed_output.explanation, True, raw_json_output
    
    except APIError as e:
        return None, f"API Error: {e}", False, str(e)
    except Exception as e: # Catches Pydantic validation errors or general parsing issues
        # Try to extract the JSON output even if validation failed
        return None, f"JSON/Parsing Error: {e}", False, response.text if 'response' in locals() else "N/A"

# 4. Prompting Strategies and Execution
# ----------------------------------------------------------------------

# --- V1: Zero-Shot (Baseline) ---
PROMPT_V1 = """
You are a highly reliable sentiment classification system.
Analyze the following Yelp review and predict the star rating (1 to 5) based on the overall sentiment.
Provide a brief explanation for your rating. 

Review: "{review}"
"""

# --- V2: Few-Shot with Chain-of-Thought (COT) ---
# Rationale: Adding examples and guiding the model's logic improves accuracy.
FEW_SHOT_EXAMPLE = """
Example 1:
Review: "The atmosphere was great, but the service was so slow we almost walked out. The food was mediocre at best."
Predicted Output (Logic: Mixed review, negative service/food heavily weighs down positive atmosphere): 2

Example 2:
Review: "Best pizza I've ever had! Every bite was perfect and the staff were friendly and attentive."
Predicted Output (Logic: Overwhelmingly positive language like 'Best,' 'perfect,' 'friendly'): 5
"""

PROMPT_V2 = f"""
You are an expert sentiment analyst. Your task is to classify Yelp reviews into 1-5 stars.
Use the following examples to guide your reasoning process:

{FEW_SHOT_EXAMPLE}

Now, analyze this new review. First, consider the key positive and negative points, then determine the final star rating.
Provide the brief reasoning in the 'explanation' field of the JSON.

Review: "{{review}}"
"""

# --- V3: Role-Play and Constraint Focus ---
# Rationale: Assigning a strict role and constraint focuses the model on format adherence and reliability.
PROMPT_V3 = """
SYSTEM INSTRUCTION: You are a **strict machine validation agent** that only outputs JSON. 
Your primary purpose is to classify the provided Yelp review into a 1-5 star rating and provide a brief justification.
Focus ONLY on the content of the review and STRICTLY adhere to the requested JSON format.

Review: "{review}"
"""

# Dictionary to hold the prompt versions and their results columns
PROMPT_VERSIONS = {
    1: {'prompt': PROMPT_V1, 'tag': 'Zero-Shot'},
    2: {'prompt': PROMPT_V2, 'tag': 'Few-Shot + COT'},
    3: {'prompt': PROMPT_V3, 'tag': 'Role-Play + Constraint'}
}

# --- Execution Loop ---
print("\n--- Starting LLM Classification for 3 Prompt Versions ---")
for version, data in PROMPT_VERSIONS.items():
    v = str(version)
    print(f"\nRunning Version {v}: {data['tag']}...")
    
    results_df[f'V{v}_Predicted'] = None
    results_df[f'V{v}_JSON_Valid'] = False
    
    for index, row in results_df.iterrows():
        predicted, explanation, is_valid, raw_output = get_llm_prediction(data['prompt'], row['review_text'])
        
        results_df.loc[index, f'V{v}_Predicted'] = predicted
        results_df.loc[index, f'V{v}_JSON_Valid'] = is_valid
        
        # Store the explanation/error message for the report
        results_df.loc[index, f'V{v}_Explanation'] = explanation
        
        # Implement a slight delay to respect API rate limits
        time.sleep(0.1)

print("\n--- All LLM executions complete. ---")


# 5. Evaluation and Comparison
# ----------------------------------------------------------------------

# Helper function to calculate accuracy and validity
def calculate_metrics(df, version):
    # JSON Validity Rate (across ALL attempts)
    json_validity_rate = df[f'V{version}_JSON_Valid'].mean()
    
    # Accuracy: Compare predicted vs actual stars, but only on VALID JSON outputs
    valid_df = df[df[f'V{version}_JSON_Valid'] == True].copy()
    
    if valid_df.empty:
        accuracy = 0.0
    else:
        # Use sklearn for robust accuracy calculation (Multiclass Accuracy)
        y_true = valid_df['actual_stars']
        y_pred = valid_df[f'V{version}_Predicted'].astype(int)
        accuracy = accuracy_score(y_true, y_pred)
        
    return accuracy, json_validity_rate

# Calculate metrics for all versions
metrics = {}
for v in PROMPT_VERSIONS:
    acc, val = calculate_metrics(results_df, v)
    metrics[v] = {'Accuracy': f'{acc:.2%}', 'JSON Validity Rate': f'{val:.2%}'}

# Create Comparison Table
comparison_data = {
    'Approach': [PROMPT_VERSIONS[1]['tag'], PROMPT_VERSIONS[2]['tag'], PROMPT_VERSIONS[3]['tag']],
    'Accuracy (on Valid JSON)': [metrics[1]['Accuracy'], metrics[2]['Accuracy'], metrics[3]['Accuracy']],
    'JSON Validity Rate': [metrics[1]['JSON Validity Rate'], metrics[2]['JSON Validity Rate'], metrics[3]['JSON Validity Rate']],
    'Prompt Change Rationale': ['Baseline comparison.', 'Added Few-Shot examples to improve classification logic.', 'Added strict role/constraint to maximize reliability.']
}
comparison_df = pd.DataFrame(comparison_data)

print("\n## Evaluation Comparison Table")
print("--------------------------------------------------")
print(comparison_df.to_markdown(index=False))
print("--------------------------------------------------")

# Display a sample of the results for visual inspection of consistency/reliability
print("\n## Sample Results (Actual vs Predicted Stars)")
sample_results = results_df[['actual_stars', 'V1_Predicted', 'V2_Predicted', 'V3_Predicted']].head(5)
print(sample_results.to_markdown(index=False))


# 6. Discussion and Conclusion (Required for Report)
# ----------------------------------------------------------------------

# **NOTE**: Fill in this section with your analysis after running the code.

print("\n## Discussion: Approach, Design Decisions, and System Behavior")
print("----------------------------------------------------------------------")
print("""
### Approach Summary
The experiment used the Gemini API with structured output defined by Pydantic (ReviewPrediction schema). 
This engineering choice was made to ensure a near-100% JSON validity rate, as Gemini's API supports robust JSON generation when a schema is provided. 
Three distinct prompts were tested against a sampled set of 200 reviews.

### Design Decisions and Prompt Iterations

1.  **V1 (Zero-Shot)**: Served as the unguided baseline. Its simplicity provides a measure of the model's inherent ability to perform the task.
2.  **V2 (Few-Shot + COT)**: This version aimed to improve **Accuracy** by offering in-context learning. The explicit examples guide the model on how to interpret nuances and map sentiment to stars, often leading to better performance in classification tasks.
3.  **V3 (Role-Play + Constraint)**: This version was designed to test the model's adherence to rules. By assigning a 'strict machine validation agent' role, it prioritizes reliable formatting over creative output, though accuracy might suffer if the rigid role prevents nuanced analysis.

### Evaluation and System Behavior

* **JSON Validity Rate**: Due to the use of Pydantic and `response_mime_type="application/json"`, the JSON Validity Rate for all three versions is expected to be extremely high (ideally 100%). Any failure indicates an issue like an API call error or the model generating a non-integer for the stars field, which is a key measure of **Reliability**.
* **Accuracy**: *(Based on the run results)* The **Few-Shot + COT (V2)** approach is typically the winner in classification accuracy because the examples provide the necessary context to handle complex, mixed-sentiment reviews.
* **Consistency**: V3 should show the most consistent *format adherence*, whereas V2 shows the most consistent *classification logic* due to the explicit reasoning guide in the prompt.

### Conclusion
The most effective approach balances high **Accuracy** (achieved by V2's guided reasoning) and high **Reliability** (guaranteed by the structured output setup).
""")
# ----------------------------------------------------------------------

# Final check of the results file structure (for submission)
# print("\nFinal Results DataFrame Head:")
# print(results_df.head().to_markdown(index=True))