from flask import Flask, render_template, redirect, url_for, request
from utils.security import verify_username
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        if request.form["signup-login"] == "Login":
            print("LOGIN NOW!!")
            return redirect(url_for("login"))

    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form["submit"] == "Back":
            return redirect(url_for("home_page"))
        if request.form["username"]:
            with open("passwords.txt", "r", encoding="utf-8") as f:
                users = [line.strip().split(" ") for line in f.readlines()]
                
    return render_template("login.html", error=error)


@app.route("/signup", methods=["GET", "POST"])
def sign_up():
    errors = None
    if request.method == "POST":
        if request.form["submit"] == "Back":
            return redirect(url_for("home_page"))

        if request.form["username"]:
            f = open("passwords.json")
            data = json.loads(f.read())
            f.close()
            errors = verify_username(request.form["username"], data)
        else:
            errors = ["Username cannot be blank"]
                
    return render_template("signup.html", errors=errors)

if __name__ == "__main__":
    app.run(debug=True)