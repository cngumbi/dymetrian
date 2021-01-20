import os
from flask import render_template, url_for, flash, redirect, request
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
