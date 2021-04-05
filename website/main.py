from flask import Flask, redirect, url_for
import json
app = Flask(__name__)
with open("config.json","r") as file:
    cntnt = file.read()
    jso = json.loads(cntnt)
    adminpass = jso["adminpass"]
@app.route("/")
def home():
    return "<h1>Hey!</h1>\nWelcome to the site!<br>There's nothing here right now. Maybe you should check back later?"
@app.route(f"/{adminpass}")
def admin():
    return "Secret ;)"
if __name__ == "__main__":
    app.run()
