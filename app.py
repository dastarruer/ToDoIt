from flask import Flask, render_template, redirect, request, session, url_for
import sqlite3
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


def isNull(parameter):
    if not parameter:
        return True
    return False


def isUserValid(user: list, password: str):
    # If there is no user with the given username, or the password was inputted incorrectly
    if len(user) < 1 or not check_password_hash(user[0]["hash"], password):
        return False
    return True


def get_db_connection():
    """Return a connection to the database"""
    conn = sqlite3.connect('tasks.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/', methods=['GET','POST', 'PATCH'])
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
        db.execute("INSERT INTO tasks (user_id, title, description) VALUES(?, ?, ?)", (session["user_id"], title, description))

        conn.commit()

        # This ensures that the browser does not ask for form resubmission after reloading the page
        return redirect(url_for("index"))

    # If the user requests to change the status of their tasks
    elif request.method == "PATCH":
        UNFINISHED = 0
        FINISHED = 1

        task_id = request.form["task-id"]
        current_task_status_code = request.form["status"]

        # If the task is unfinished, set the task's status code to finished, otherwise set it to finished
        new_task_status_code = FINISHED if current_task_status_code == UNFINISHED else UNFINISHED

        # Change the task's status in the database
        db.execute("UPDATE tasks SET completed = ? WHERE id = ?", (new_task_status_code,task_id))

        conn.commit()
        conn.close()

        return redirect(url_for("index"))
    
    tasks = db.execute("SELECT title, description FROM tasks WHERE user_id = ?", [session["user_id"]]).fetchall()


    conn.close()

    return render_template("index.html", tasks=tasks)

# TODO: Return an error if there is a duplicate username
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

        conn.close()  

        return render_template("login.html")     
    return render_template("register.html")

@app.route("/login", methods=['GET','POST'])
def login():
    # Forget user id
    session.clear()

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        if isNull(username) or isNull(password):
            error = "Username/Password cannot be empty"
            return render_template("login.html", error=error)

        conn = get_db_connection()
        db = conn.cursor()

        # Query database for username
        user = db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchall()

        conn.close()

        if not isUserValid(user, password):
            error = "Invalid credentials, please try again"
            return render_template("login.html", error=error)
        
        # Set the user id to the current user's id, so that the page remembers them
        session["user_id"] = user[0]["id"]

        return redirect("/")
    return render_template("login.html")

if __name__ == "__app.py__":
    app.run(debug=True)