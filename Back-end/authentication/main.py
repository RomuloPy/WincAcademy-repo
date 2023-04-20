import os

from flask import Flask, redirect, render_template, request, session, url_for
from helpers import get_users, hash_password

__winc_id__ = "8fd255f5fe5e40dcb1995184eaa26116"
__human_name__ = "authentication"

app = Flask(__name__)

app.secret_key = os.urandom(16)


@app.route("/home")
def redirect_index():
    return redirect(url_for("index"))


@app.route("/")
def index():
    return render_template("index.html", title="Index")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/lon")
def lon():
    return render_template("lon.html", title="League of Nations")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        session["username"] = request.form["username"]
        session["password"] = request.form["password"]

        print(session["username"])
        print(session["password"])

        # if login is valid
        if valid_login(session["username"], session["password"]):
            return redirect("/dashboard")

        else:
            error = "Invalid_Login"
            return redirect(f"/login?error={error}")

    return render_template("login.html", title="Login")


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    # YOUR SOLUTION HERE
    if request.method == "POST":
        return redirect("/logout")

    return render_template("dashboard.html", title="Dashboard")


@app.route("/logout")
def logout():
    # YOUR SOLUTION HERE
    session.pop('username', None)
    return redirect(url_for('index'))
