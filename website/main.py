from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hey!</h1>\nWelcome to the site!"

@app.route("/$(HIToidni0I$R$TLEnqDLFKQP$(R@JM")
def admin():
    return "Admins only! Beware!"
if __name__ == "__main__":
    app.run()
