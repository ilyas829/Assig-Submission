from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return("Please use '/home' to redirect to Home page!<br> Thank you <br><a href='http://127.0.0.1:5000/home'>Click Here</a>")

@app.route("/home")
def home_page():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)