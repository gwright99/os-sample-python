from flask import Flask
application = Flask(__name__)


@application.route("/")
def hello():
    return "Hello World!"


@application.route("/newendpoint")
def newendpoint():
	return "This is a new endpoint I added on my local machine, pushed to Github, and then rebuilt via OpenShift S2i"


if __name__ == "__main__":
    application.run()
