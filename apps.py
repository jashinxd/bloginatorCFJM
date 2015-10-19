from flask import Flask, render_template, request, session, redirect, url_for
import utils

app = Flask(__name__)
@app.route("/")
@app.route("/home")
def home():
    if button == "Cancel":
        return render_template("home.html", link = "/login", state = "Login")
    if button == "Post":
        post = request.form['story']
        return render_template("login.html", link = "/login", state = "Login")
    return render_template("home.html", link = "/login", state = "Login")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html", link = "/login", state = "Login")
    else:
        uname = request.form['username']
        pword = request.form['password']
        button = request.form['button']
        if button == "cancel":
            return render_template("login.html", link = "/login", state = "Login")
        if utils.authenticate(uname,pword):
            session['user'] = uname
            return redirect(url_for("home", link = "/login", state = "Login"))
        else:
            if utils.validuname(uname):
                error = "Username and password do not match."
                return render_template("login.html", err = error, link = "/login", state = "Login")
            else:
                error = "Username not in our database."
                return render_template("login.html", err = error, link = "/login", state = "Login")

@app.route("/logout")
def logout():
    session['user'] = 0
    print (session['user'])
    return redirect(url_for("log_in", link = "/login", state = "Login"))
    

@app.route("/about")
def about():
    return render_template("about.html", link = "/login", state = "Login")


@app.route("/contact")
def contact():
    return render_template("contact.html", link = "/login", state = "Login")

@app.route("/register", methods=["GET","POST"])
def register(): 
    if request.method == "GET":
        return render_template("register.html", link = "/login", state = "Login")
    else:
        uname = request.form['username']
        pword = request.form['password']
        button = request.form['button']
        age = request.form['age']
        gender = request.form['gender']
        if button == "cancel":
            return render_template("register.html", link = "/login", state = "Login")
        if utils.validuname(uname):
            error = "Username already exists. Please try again."
            return render_template("register.html", err = error)
        if uname == "" or pword == "" or age == "" or gender == "":
            error = "All fields must be filled in. Please try again."
            return render_template("register.html", err = error, link = "/login", state = "Login")
        else:
            utils.register(uname, pword, age, gender)
            return render_template("login.html", link = "/login", state = "Login")
    
if __name__ == "__main__":
    app.debug = True
    app.secret_key = "Don't put on git"
    app.run(host="0.0.0.0", port=8700)
