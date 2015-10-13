from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")
