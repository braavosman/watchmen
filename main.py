from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_w():
    return "Hello World!"

@app.route("/hello")
def hello():
    return "Hello hello"

if __name__ == "__main__":
    app.run()
