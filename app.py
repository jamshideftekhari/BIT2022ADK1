from flask import Flask
from flask import render_template
from datetime import datetime
from Repository import Repository


app = Flask(__name__)
Repo = Repository() 
Repo.SetConnection()
@app.route("/") 
def home():
    return render_template("index.html", timenow=str(datetime.now()))

@app.route("/Search/") 
def MaxWind():
    return "Under construction = "

@app.route("/Students/") 
def WindData():
    data = Repo.GetAllTolist()
    return render_template("students.html", stdata=data)  
app.run()  