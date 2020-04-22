import datetime
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route("/")
def date():
	now = datetime.datetime.now()
	new_year = now.month == 1 and now.day == 1
	return render_template("hello.html", new_year=new_year)

@app.route("/name", methods = ["POST"])
def name():
	name = request.form.get("name")
	return render_template("name.html", name=name)

@app.route("/more")
def more():
	return render_template("more.html")
