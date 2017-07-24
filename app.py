from flask import Flask, render_template , request
import random 



app = Flask(__name__)

@app.route("/")
def homepage():
	return render_template("homepage.html")

@app.route("/aboutus")
def aboutus():
	return render_template("aboutus.html")

@app.route("/contactus")
def contactus():
	return render_template("contactus.html")

@app.route("/south")
def southpage():
	return render_template("south.html")

@app.route("/north")
def northpage():
	return render_template("north.html")

@app.route("/east")
def eastpage():
	return render_template("east.html")

@app.route("/west")
def westpage():
	return render_template("west.html")




if (__name__)==("__main__"):
	app.run()