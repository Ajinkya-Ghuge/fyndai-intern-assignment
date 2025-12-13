# 🤖 AI Feedback & Rating Prediction System

An end-to-end AI-powered system built as part of the **FYND AI Intern Take-Home Assessment**, consisting of:

- **Task 1:** Yelp review star-rating prediction using prompt engineering  
- **Task 2:** A two-dashboard AI feedback web application using Flask and Gemini LLM  

---

## 📌 Table of Contents

- [Project Overview](#project-overview)
- [Task 1 – Rating Prediction via Prompting](#task-1--rating-prediction-via-prompting)
- [Task 2 – Two-Dashboard AI Feedback System](#task-2--two-dashboard-ai-feedback-system)
- [Tech Stack](#tech-stack)
- [Installation & Setup](#installation--setup)
- [Running the Application](#running-the-application)
- [Environment Variables](#environment-variables)
- [Project Structure](#project-structure)
- [Database Schema](#database-schema)
- [Deployment](#deployment)
- [Evaluation Summary](#evaluation-summary)
- [License](#license)

---

## 🚀 Project Overview

This project demonstrates practical applications of **Large Language Models (LLMs)** in:

1. Predicting numeric ratings from free-text reviews  
2. Building a real-world AI-powered feedback analysis system  

The system uses **Google Gemini (2.5 Flash)** for all LLM-based components and stores data in a shared **SQLite database**.

---

## 🧠 Task 1 – Rating Prediction via Prompting

### Objective
Predict **1–5 star ratings** from Yelp review text using prompt engineering techniques, without model fine-tuning.

### Dataset
- Yelp Reviews dataset (Kaggle)
- Random sample of **200 reviews**
- Fields: `text`, `stars`

### Prompting Strategies

| Version | Strategy | Description |
|------|---------|-------------|
| V1 | Zero-Shot | Basic sentiment-to-rating mapping |
| V2 | Few-Shot + CoT | In-context examples with reasoning |
| V3 | Role-Play + Constraints | Strict JSON output with validation |

Each approach returns structured JSON using a Pydantic schema.

### Results

| Prompt Version | Accuracy | JSON Validity |
|--------------|----------|---------------|
| Prompt_V1 | 34.5% | 100% |
| Prompt_V2 | 34.0% | 100% |
| Prompt_V3 | **35.0%** | 100% |

Prompt_V3 achieved the best overall performance.

---

## 🌐 Task 2 – Two-Dashboard AI Feedback System

### Objective
Build a web-based feedback platform with:
- A **User Dashboard** for submitting reviews
- An **Admin Dashboard** for monitoring AI-generated insights

### System Flow

1. User submits a star rating and review  
2. Review is sent to the Gemini LLM  
3. AI generates:
   - Friendly user reply  
   - One-line summary  
   - Actionable recommendations  
4. Data is stored in SQLite  
5. Admin dashboard displays all submissions

---

## 🛠 Tech Stack

**Backend**
- Python
- Flask
- SQLite

**AI / LLM**
- Google Gemini 2.5 Flash
- `google-generativeai`

**Frontend**
- HTML
- Bootstrap

**Deployment**
- Gunicorn
- Heroku-compatible Procfile

---

## ⚙️ Installation & Setup

```bash
git clone <repository-url>
cd <project-folder>

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirement.txt
python app.py
.
├── app.py
├── task1.py
├── utils/
│   └── gemini_llm.py
├── templates/
│   ├── user.html
│   └── admin.html
├── database/
│   └── submissions.db
├── requirement.txt
├── Procfile
├── .env
└── TASK 1 and 2 Report.pdf
