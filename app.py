from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def root():
    return render_template('index.html')

@app.route("/home")
def home():
    return "welcome to home pages"


@app.route("/success/<int:score>")
def success(score):
    return "You pass this exam "+ str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return "You fail this exam "+ str(score)

@app.route("/result/<int:marks>")
def results(marks):
    result=""
    if marks < 50:
        result =  'fail'

    else:
        result = 'success'
    return redirect(url_for(result,score=marks))

# submit
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)