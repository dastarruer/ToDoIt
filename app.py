from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

USER_ID = 1


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

        # Check if the title is empty
        if title == "":
            # Just redirect the user to the main page, so that nothing gets added to their tasks
            return redirect("/")

        # Add the task to the database
        db.execute("INSERT INTO tasks (user_id, title, description) VALUES(?, ?, ?)", (USER_ID, title, description))

        # Finalize the transaction
        conn.commit()

        # This ensures that the browser does not ask for form resubmission after reloading the page
        return redirect(url_for("index"))

    # Get all the user's tasks  
    tasks = db.execute("SELECT title, description FROM tasks WHERE user_id = ?", [USER_ID]).fetchall()

    conn.close()

    return render_template("index.html", tasks=tasks)

@app.route("/register")
def register():
    return render_template("register.html")