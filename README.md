# Fynd AI Intern – Take Home Assessment 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-green.svg)](https://flask.palletsprojects.com/)
[![Gemini](https://img.shields.io/badge/Gemini-2.5_Flash-orange.svg)](https://ai.google.dev/gemini-api)

This repository contains my complete solution for the **Fynd AI Intern Take Home Assessment**, covering both required tasks. Both tasks leverage LLMs (Gemini API – free tier) and emphasize real-world AI system design, evaluation, and deployment.

## 📋 Table of Contents
- [Tech Stack](#tech-stack)
- [Task 1 – Rating Prediction via Prompting](#task-1--rating-prediction-via-prompting)
- [Task 2 – Two-Dashboard AI Feedback System](#task-2--two-dashboard-ai-feedback-system)
- [How to Run Locally](#how-to-run-locally)
- [Deployment](#deployment)
- [Design Highlights](#design-highlights)
- [Conclusion](#conclusion)
- [Author](#author)
- [Contributing](#contributing)
- [License](#license)

## Tech Stack 🛠️
| Category       | Technologies                          |
|----------------|---------------------------------------|
| **Language**   | Python                                |
| **LLM**        | Gemini 2.5 Flash (Free Tier)          |
| **Backend**    | Flask                                 |
| **Frontend**   | HTML, CSS, Bootstrap 5                |
| **Database**   | SQLite                                |
| **Notebook**   | Jupyter Notebook                      |
| **Deployment** | Render / HuggingFace Spaces / Vercel (as applicable) |

## Task 1 – Rating Prediction via Prompting 📊

### Objective
Predict Yelp review star ratings (1–5 stars) using prompt-based LLM classification, and return structured JSON output.

### Output Format
The LLM outputs predictions in structured JSON:
```json
{
  "predicted_stars": 4,
  "explanation": "Brief reasoning for the assigned rating."
}
Dataset

Source: Yelp Reviews Dataset (Kaggle)
File Used: yelp.csv
Rows Sampled: ~200 reviews (for evaluation efficiency)

Prompting Approaches
Three different prompting strategies were implemented:

Prompt v1 – Basic Classification
Simple instruction to classify review into stars.
Minimal constraints.
Prompt v2 – Guided Prompt
Explicit guidance on sentiment and rating mapping.
Improved consistency.
Prompt v3 – Rubric-Based Prompt
Clear star-level rubric (1–5).
Enforced JSON-only response.

Evaluation Metrics
Each prompt was evaluated on:

Accuracy: Actual stars vs predicted stars
JSON Validity Rate: Correctly formatted JSON responses
Reliability: Consistency across similar reviews

Findings





























Prompt VersionAccuracyJSON ValidityConsistencyv1 BasicLow–MediumMediumLowv2 GuidedMediumHighMediumv3 RubricHighVery HighHigh
✅ Structured prompts with explicit rubrics significantly improved output quality.
Notebook Location
texttask1/
└── rating_prediction_prompting.ipynb
Task 2 – Two-Dashboard AI Feedback System 🖥️
Objective
Build a web-based system with:

User Dashboard: Submit reviews & get AI replies
Admin Dashboard: View all feedback with AI insights

System Architecture
textUser → Flask App → Gemini LLM
               ↓
            SQLite DB
               ↓
         Admin Dashboard
Both dashboards share the same data source.
User Dashboard (Public-Facing) 👤
Users can:

Select star rating
Write a review
Submit feedback

On submission:

AI-generated reply is shown instantly
Feedback is stored in the database

Admin Dashboard (Internal-Facing) ⚙️
Displays:

Star rating
User review
AI-generated summary
AI-suggested recommended actions

Additional UX enhancements:

Styled AI action cards
Star visualization
Responsive table layout
Optional CSV/Excel export

LLM Usage in Task 2 🤖
LLM is used for:

✅ User-facing response generation
✅ Review summarization
✅ Recommended next actions

Data Storage

SQLite database
Single shared DB for both dashboards
Zero external DB setup required

How to Run Locally 🏠

Clone the repository:textgit clone https://github.com/yourusername/fynd-ai-intern-assessment.git
cd fynd-ai-intern-assessment
Install dependencies:textpip install -r requirements.txt
Set environment variables:textexport GEMINI_API_KEY="your_api_key_here"
Run the application:textpython app.py
Open in browser:
User Dashboard: http://127.0.0.1:5000
Admin Dashboard: http://127.0.0.1:5000/admin


Deployment 🚀
Both dashboards are deployed and accessible via public URLs.
(Links provided in final submission)
Design Highlights 🎨

Minimalistic and responsive UI
Graceful handling of LLM rate limits
Clean separation of user and admin functionality
Real-world feedback workflow simulation

Conclusion 📝
This project demonstrates:

Prompt engineering experimentation and evaluation
Practical LLM integration in a production-like system
Full-stack deployment of AI-powered applications

The solution satisfies all requirements of the Fynd AI Intern Take Home Assessment.
Author 👨‍💻
Ajinkya
B.Tech Computer Science
AI & Data Science Enthusiast 🚀
LinkedIn | Portfolio | Email
Contributing 🤝
Contributions welcome! Please open an issue or PR for bugs, features, or improvements. Follow the code of conduct.
License 📄
This project is licensed under the MIT License - see the LICENSE file for details.
