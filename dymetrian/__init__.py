from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)
@app.route("/")
@app.route("/home")
def dymetrian():
    return render_template('index.html')