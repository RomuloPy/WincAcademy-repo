__winc_id__ = "cc1b724762854e85a8defa04287f708b"
__human_name__ = "requests"

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/greet")
def greet():
    return render_template("greet.html")


@app.route("/greet/<example_name>")
def greet_name(example_name):
    return render_template("greet_example_name.html", example_name=example_name)


if __name__ == "__main__":
    app.run(debug=True)
