from flask import Flask, render_template, request, jsonify
import sqlite3, time, os, json
from utils.gemini_llm import user_reply, summary_and_actions

app = Flask(__name__)

# ---------- DB SETUP ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, "database")
os.makedirs(DB_DIR, exist_ok=True)
DB = os.path.join(DB_DIR, "submissions.db")
# -------------------------------

def init_db():
    with sqlite3.connect(DB) as con:
        con.execute("""
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rating INTEGER,
            review TEXT,
            ai_reply TEXT,
            summary TEXT,
            actions TEXT,
            created_at REAL
        )
        """)

@app.route("/")
def user_page():
    return render_template("user.html")

@app.route("/submit", methods=["POST"])
def submit():
    rating = request.form["rating"]
    review = request.form["review"]

    reply = user_reply(review, rating)
    sa = summary_and_actions(review)

    with sqlite3.connect(DB) as con:
        con.execute("""
        INSERT INTO submissions
        (rating, review, ai_reply, summary, actions, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            rating,
            review,
            reply,
            sa["summary"],
            json.dumps(sa["actions"]),
            time.time()
        ))

    return jsonify({"ai_reply": reply})

@app.route("/admin")
def admin():
    # just read name from query param, no password
    admin_name = request.args.get("name", "Admin")

    with sqlite3.connect(DB) as con:
        con.row_factory = sqlite3.Row
        rows = con.execute(
            "SELECT * FROM submissions ORDER BY created_at DESC"
        ).fetchall()

    return render_template("admin.html", data=rows, admin_name=admin_name)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
