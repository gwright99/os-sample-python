from flask import Flask
import mysql.connector

application = Flask(__name__)


@application.route("/")
def hello():
    return "Hello World!"


@application.route("/newendpoint")
def newendpoint():
	return "This is a new endpoint I added on my local machine, pushed to Github, and then rebuilt via OpenShift S2i"


@application.route("/get_dbs")
def get_dbs():
	mydb = mysql.connector.connect(host="mysql-python", user="user1", password="mypa55")
	c = mydb.cursor()
	c.execute("show databases")
	dbs = ','.join(str(x[0]) for x in c)
	return f"Databases are: {dbs}."


if __name__ == "__main__":
    application.run()
