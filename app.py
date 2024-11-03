from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_session import Session
from werkzeug.security import generate_password_hash

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

USER_ID = 1


def isNull(parameter):
    if parameter == "":
        return True
    return False


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

        if isNull(title):
            # Just redirect the user to the main page, so that nothing gets added to their tasks
            return redirect("/")

        # Add the task to the database
        db.execute("INSERT INTO tasks (user_id, title, description) VALUES(?, ?, ?)", (USER_ID, title, description))

        conn.commit()

        # This ensures that the browser does not ask for form resubmission after reloading the page
        return redirect(url_for("index"))

    tasks = db.execute("SELECT title, description FROM tasks WHERE user_id = ?", [USER_ID]).fetchall()

    conn.close()

    return render_template("index.html", tasks=tasks)

@app.route("/register", methods=['GET','POST'])
def register():
    if request.method == "POST":
        conn = get_db_connection()
        db = conn.cursor()

        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["confirm-password"]

        if isNull(username) or isNull(password):
            error = "Username/Password cannot be empty"
            return render_template("register.html", error=error)

        elif password != confirm_password:
            error = "Password must be same as Confirm Password"
            return render_template("register.html", error=error)
        
        # Hash the password
        hash = generate_password_hash(password, salt_length=8)

        # Add the user to the database
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", (username, hash))

        # Finalize the transaction
        conn.commit()        
    return render_template("register.html")