from flask import Flask, render_template, request

app = Flask(__name__)

TASKS = []

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # Get the title and description of the task the user wants to add
        title = request.form['title']
        description = request.form['description']

        # Append the task to TASKS
        TASKS.append({"title" : title, "description" : description})
    return render_template("index.html", tasks=TASKS)