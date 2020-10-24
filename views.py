#from __init__ import app

from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__, template_folder='templates')
app.static_folder = 'static'
app.secret_key = "spininmanurematch"

@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("home.html")

@app.route("/randomRestaurant", methods=["POST", "GET"])
def randomRestaurant():
    return render_template("randomRestaurant.html")

if __name__ == "__main__":
    app.run(debug=True)