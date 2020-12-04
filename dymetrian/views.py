from flask import Flask, render_template, url_for, redirect, request

#custome modules
from dymetrian import app

@app.route("/")
@app.route("/home")
def dymetrian():
    return render_template('index.html')


@app.route("/about/")
def about():
    return render_template('aboutUs.html')


@app.route("/products/")
def products():
    return render_template('elements.html')