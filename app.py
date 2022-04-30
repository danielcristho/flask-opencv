import imp
from flask import Flask

app = Flask(__name__)

@app.route("/home")
def home():
    return "welcome home"

@app.route("/base")
def base():
    return "Member pages"    

@app.route("/success/<int:score>")
def success(score):
    return "You pass this exam "+ str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return "You fail this exam "+ str(score)

if __name__ == '__main__':
    app.run(debug=True)