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
	user_fullname = request.form["fullname"]
	user_email = request.form["email"]
	user_restaurantname = request.form["restaurantname"]
	user_recomindation = request.form["recomindation"]
#	info_table.insert(dict(fullname= user_fullname, useremail=user_email, restaurantname=user_restaurantname, userrecomindation=user_recomindation))
	# return info_table.find_one(firname="khaled")
	
	return render_template("veiwtheuser.html" ,
		fullname= user_fullname,
		useremail=user_email,
		restaurantname=user_restaurantname,
		userrecomindation=user_recomindation
		) 


if (__name__)==("__main__"):
	app.run()