from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("hello.html")

@app.route("/test")
def testing():
    return "test this one is this working "

if __name__ == "__main__":
    app.run(debug=True)
