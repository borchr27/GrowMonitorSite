# app.py
from flask import Flask, render_template  # importing the render_template function

app = Flask(__name__)
# home route
@app.route("/home")
def Home():
    return render_template('home.html')

@app.route("/contact")
def Contact():
    return render_template('contact.html')

@app.route("/about")
def About():
    return render_template('about.html')

app.run(debug = True) 