import google.generativeai as genai
import os, json, re
from dotenv import load_dotenv

load_dotenv()  # 👈 THIS LINE WAS MISSING

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def user_reply(review, rating):
    prompt = f"""
Customer gave {rating} stars.
Review: "{review}"

Write ONLY ONE short friendly business reply.
Do not give options.
Do not explain.

"""
    return model.generate_content(prompt).text.strip()

def summary_and_actions(review):
    prompt = f"""
You are an internal product manager.

Analyse the customer review and return ONLY valid JSON.
Be very concise.

Rules for actions:
- Max 2–3 actions only
- Each action must be 2–4 words
- No full sentences
- Action-oriented and practical

JSON format ONLY:
{{
  "summary": "very short one-line summary",
  "actions": ["short action 1", "short action 2"]
}}

Review: "{review}"
"""

    response = model.generate_content(prompt).text.strip()
    match = re.search(r"\{.*\}", response, re.DOTALL)
    return json.loads(match.group())

