# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import month_choice_message
import model


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/results', methods = ["GET", "POST"])
def results():
    print (request.form["birthstone"])
    # props = {
    #     'sound': 'roar'
    # }
    user_choice = request.form["birthstone"]
    message = month_choice_message(user_choice)
    return render_template("results.html", message = message)

