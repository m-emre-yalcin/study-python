from flask import Flask

app = Flask("rest-api")


@app.route("/")
def hello_world():
    return "<h1>Hello world!</h1>"
