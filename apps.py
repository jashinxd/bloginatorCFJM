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
                return render_template("login.html", err = error)
            else:
                error = "Username not in our database."
                return render_template("login.html", err = error)
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/register", methods=["GET","POST"])
def register(): 
    if request.method == "GET":
        return render_template("register.html")
    else:
        uname = request.form['username']
        pword = request.form['password']
        button = request.form['button']
        age = request.form['age']
        gender = request.form['gender']
        if button == "cancel":
            return render_template("register.html")
        if utils.validuname(uname):
            error = "Username already exists. Please try again."
            return render_template("register.html", err = error)
        if uname == "" or pword == "" or age == "" or gender == "":
            error = "All fields must be filled in. Please try again."
            return render_template("register.html", err = error)
        else:
            utils.register(uname, pword, age, gender)
            return render_template("login.html")
    
if __name__ == "__main__":
    app.debug = True
    app.secret_key = "Don't put on git"
    app.run(host="0.0.0.0", port=8700)
