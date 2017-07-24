from flask import Flask, render_template , request
import random 
import dataset


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

@app.route("/contactus")
def contact_us():
	return render_template("contactus.html")


@app.route("/viewtheuser", methods= ["POST"])
def hello():
	user_name = request.form["firstname"]
	user_lastname = request.form["lastname"]
	user_message = request.form["message"]
	user_gender = request.form["gender"]
	# info_table.insert(dict(firname="user_name" , lasname="user_lastname", message="user_message" , gender= "user_info"))
	# return info_table.find_one(firname="khaled")
	
	return render_template("veiwtheuser.html" ,
		username= user_name,
		userlastname=user_lastname,
		usermessage=user_message,
		usergender=user_gender
		) 


if (__name__)==("__main__"):
	app.run()