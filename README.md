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
