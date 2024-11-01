from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

user_id = 1


def get_db_connection():
    """Return a connection to the database"""
    conn = sqlite3.connect('tasks.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/', methods=['GET','POST'])
def index():
    conn = get_db_connection()
    db = conn.cursor()
    if request.method == 'POST':
        # Get the title and description of the task the user wants to add
        title = request.form['title']
        description = request.form['description']

        # Add the task to the database
        db.execute("INSERT INTO tasks (user_id, title, description) VALUES(?, ?, ?)", (user_id, title, description))

        conn.commit()

        return redirect(url_for("index"))

    tasks = db.execute("SELECT title, description FROM tasks WHERE user_id = ?", [user_id]).fetchall()

    conn.close()

    return render_template("index.html", tasks=tasks)