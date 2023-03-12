from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html")

@app.route("/about")
def question():
    return "What is the meaning of life?"

if __name__ == "__main__":
    app.run(debug=True)