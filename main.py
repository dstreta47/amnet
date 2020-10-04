from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/amnet")
def amnet():
    return "Hello, amnet"

@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")
    
@app.route("/sample1")
def sample1():
    return render_template("sample1.html")
    
if __name__ == "__main__":
    app.run(debug=True)