from flask import Flask, render_template, redirect, url_for, request
from utils.security import validate_username, validate_password
import csv

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
    success = None
    errors = list()
    if request.method == "POST":
        if request.form["submit"] == "Back":
            return redirect(url_for("home_page"))

        if request.form["username"]:
            with open("passwords.txt", "r") as f:
                csv_reader = csv.reader(f, delimiter=",")
                errors += validate_username(request.form["username"], csv_reader)
        else:
            errors = ["Username cannot be blank"]

        if request.form["password"]:
            pw_errors, hash = validate_password(request.form["password"])
            errors += pw_errors
        else:
            errors = ["Password cannot be blank"]
        if not errors:
            success = "New user created!"
            with open("passwords.txt", "a") as f:
                writer = csv.writer(f)
                writer.writerow([request.form["username"], hash])
    return render_template("signup.html", errors=errors, success=success)

if __name__ == "__main__":
    app.run(debug=True)