🤖 AI Feedback & Rating Prediction System

An end-to-end AI-powered system built as part of the FYND AI Intern Take-Home Assessment, consisting of:

Task 1: Yelp review star-rating prediction using prompt engineering

Task 2: A production-ready, two-dashboard AI feedback web application using Flask and Gemini LLM

📌 Table of Contents

Project Overview

Task 1 – Rating Prediction via Prompting

Task 2 – Two-Dashboard AI Feedback System

Tech Stack

Installation & Setup

Running the Application

Environment Variables

Project Structure

Database Schema

Deployment

Evaluation Summary

License

🚀 Project Overview

This project demonstrates practical applications of Large Language Models (LLMs) in:

Natural Language → Rating prediction using structured prompting

Real-world feedback analysis with AI-generated replies, summaries, and actionable insights

The system uses Google Gemini (2.5 Flash) for all LLM-powered components and stores feedback in a shared SQLite database.

🧠 Task 1 – Rating Prediction via Prompting
🎯 Objective

Predict 1–5 star ratings from Yelp review text using prompt engineering, without fine-tuning.

📊 Dataset

Yelp Reviews dataset (Kaggle)

Random sample of 200 reviews

Fields used: text, stars

🧪 Prompting Strategies

Three prompting approaches were evaluated:

Version	Strategy	Description
V1	Zero-Shot	Basic sentiment → rating mapping
V2	Few-Shot + CoT	In-context examples with reasoning
V3	Role-Play + Constraints	Strict JSON-only, validation-focused

Each prompt returns structured JSON using a Pydantic schema.

📈 Results Summary
Prompt Version	Accuracy	JSON Validity
Prompt_V1	34.5%	100%
Prompt_V2	34.0%	100%
Prompt_V3	35.0%	100%

Prompt_V3 achieved the best balance between accuracy and reliability.
Full implementation is available in task1.py and the report .

🌐 Task 2 – Two-Dashboard AI Feedback System
🎯 Objective

Build a web-based feedback platform with:

A User Dashboard for submitting reviews

An Admin Dashboard for monitoring AI-generated insights

🔄 System Flow

User submits a rating + review

Review is sent to Gemini LLM

AI generates:

Friendly reply

One-line summary

Actionable recommendations

Data is stored in SQLite

Admin dashboard displays all feedback in real time

🧩 Core Application

Implemented in Flask (app.py)

🛠 Tech Stack

Backend

Python

Flask

SQLite

AI / LLM

Google Gemini 2.5 Flash

google-generativeai

Frontend

HTML

Bootstrap

Deployment

Gunicorn

Procfile (Heroku-ready)

Dependencies listed in requirement.txt

⚙️ Installation & Setup
# Clone repository
git clone <your-repo-url>
cd <project-folder>

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirement.txt

▶️ Running the Application
python app.py


User Dashboard → http://127.0.0.1:5000/

Admin Dashboard → http://127.0.0.1:5000/admin?name=Admin

🔐 Environment Variables

Create a .env file with:

GEMINI_API_KEY=your_gemini_api_key
ADMIN_PASSWORD=admin123


(Loaded automatically using python-dotenv)

📂 Project Structure
.
├── app.py                # Flask application
├── task1.py              # Task 1 rating prediction
├── utils/
│   └── gemini_llm.py     # LLM helper functions
├── templates/
│   ├── user.html
│   └── admin.html
├── database/
│   └── submissions.db
├── requirement.txt
├── Procfile
├── .env
└── TASK 1 and 2 Report.pdf

🗄 Database Schema

Table: submissions

Column	Type	Description
id	INTEGER	Primary key
rating	INTEGER	User rating
review	TEXT	User review
ai_reply	TEXT	LLM reply
summary	TEXT	AI summary
actions	TEXT	JSON actions
created_at	REAL	Timestamp

Defined and initialized in app.py .

☁️ Deployment

The project is Heroku-ready using:

web: gunicorn app:app


(Defined in Procfile)

📊 Evaluation Summary

✔ Reliable structured AI output (100% JSON validity)

✔ Shared database across dashboards

✔ Real-time admin visibility

✔ Clean, responsive UI

✔ Graceful handling of API rate limits

This system demonstrates real-world applicability of LLMs for feedback analysis and decision support.

📄 License

This project is submitted for educational and evaluation purposes as part of the FYND AI Intern Assessment.
