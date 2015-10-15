from flask import Flask, render_template, request, session, redirect, url_for
import utils

app = Flask(__name__)
@app.route("/")
@app.route("/home")
@app.route("/home/")
def index():
    return render_template("home.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        uname = request.form['username']
        pword = request.form['password']
        button = request.form['button']
        if button == "cancel":
            return render_template("login.html")
        if utils.authenticate(uname,pword):
            return render_template("home.html")
        else:
            if utils.validuname(uname):
                error = "Username and password do not match."
            else:
                error = "Username not in our database."
                return render_template("login.html", err = error)
@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "Don't put on git"
    app.run(host="0.0.0.0", port=8700)
