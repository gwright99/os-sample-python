from flask import Flask
import mysql.connector

application = Flask(__name__)


def get_db_connection():
	mydb = mysql.connector.connect(host="mysql-python", user="root", password="r00tpa55")
	# mydb = mysql.connector.connect(host="mysql-python", user="user1", password="mypa55")
	mycursor = mydb.cursor()
	return mycursor


@application.route("/")
def hello():
    return "Hello World!"


@application.route("/newendpoint")
def newendpoint():
	return "This is a new endpoint I added on my local machine, pushed to Github, and then rebuilt via OpenShift S2i"


@application.route("/get_dbs")
def get_dbs():
	#mydb = mysql.connector.connect(host="mysql-python", user="user1", password="mypa55")
	# mydb = get_db_connection()
	# c = mydb.cursor()
	cursor = get_db_connection()

	
	cursor.execute("show databases")
	dbs = ','.join(str(x[0]) for x in c)
	return f"\nDatabases are: {dbs}.\n"


@application.route("/create_db/<db_name>", methods=['GET'])
def create_db(db_name):
	# mydb = mysql.connector.connect(host="mysql-python", user="root", password="r00tpa55")
	# c = mydb.cursor()
	cursor = get_db_connection()

	c.execute("show databases")
	dbs = [x for x in c]

	if db_name in dbs:
		return f"\nCannot create database {db_name}; it already exists\n"
	else:
		c.execute(f"CREATE DATABASE {db_name}")
		return f"\nDatabase {db_name} created. Please confirm by using /get_dbs\n"


if __name__ == "__main__":
    application.run()
