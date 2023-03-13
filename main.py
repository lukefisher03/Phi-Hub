from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def home_page():
    # print()
    return render_template("home.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == "POST":
        if request.form["username"] != "admin" or request.form["password"] != "admin":
            error = "Invalid Creds!"
        else:
            return redirect(url_for('home_page'))
    return render_template("login.html", error=error)

if __name__ == "__main__":
    app.run(debug=True)