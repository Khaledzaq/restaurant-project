from flask import Flask, render_template , request
import random 
import dataset
# db = dataset.connect('postgres://yowahpfaxtsjoc:89e78de430594fa7bffec234ce5bc8ac9193cef0a864378fd900ddd573d65651@ec2-23-23-244-83.compute-1.amazonaws.com:5432/dbn2rcviq5s3i4')
# info_table = db["restaurant_rate"]



app = Flask(__name__)

@app.route("/")
def homepage():
	return render_template("homepage.html")

@app.route("/aboutus")
def aboutus():
	return render_template("aboutus.html")

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

@app.route("/recomendation")
def recomendation():
	return render_template("recomendation.html")


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