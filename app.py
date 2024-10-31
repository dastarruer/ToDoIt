from flask import Flask, render_template, request

app = Flask(__name__)

TASKS = []

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        TASKS.append({"title" : title, "description" : description})    
    return render_template("index.html", tasks=TASKS)

