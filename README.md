Fynd AI Intern – Take Home Assignment

This repository contains my solution for the Fynd AI Intern Take Home Assessment, covering both required tasks.

Task 1 – Rating Prediction via Prompting

Dataset: Yelp Reviews (Kaggle)

Goal: Predict 1–5 star ratings from review text using LLM prompts

Implemented 3 different prompt strategies

Compared performance on:

Accuracy (actual vs predicted stars)

JSON validity

Output consistency

Evaluation done on a sampled subset (~200 reviews)

Implemented in a Jupyter Notebook

Output Format

{
  "predicted_stars": 4,
  "explanation": "Brief reasoning for the rating"
}

Task 2 – Two-Dashboard AI Feedback System

A web-based application with two dashboards:

User Dashboard (Public)

Submit star rating + review

Receive AI-generated response

Feedback stored in database

Admin Dashboard (Internal)

View all submissions

See AI-generated summaries & recommended actions

Responsive, clean UI with enhanced readability

Tech Stack

Python, Flask

Gemini 2.5 Flash (Free Tier)

HTML, CSS, Bootstrap

SQLite

Jupyter Notebook

LLM Usage

Review classification (Task 1)

User-facing replies

Review summarization

Recommended next actions

Deployment

Both dashboards are deployed and accessible via public URLs

All required links are included in the final submission

Author

Ajinkya – B.Tech Computer Science
AI & Data Science Enthusiast 🚀
