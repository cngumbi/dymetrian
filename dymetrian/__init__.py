import os
from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager


#custome modules
from config import Configuration



app = Flask(__name__)
"""APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))                   #applicatioon directory
DEBUG = True 
SECRET_KEY = '&\xfb?\xfbL\xd7\xc0z\x19ewF\xdd\xe6\xce(M\xbc\x15,'
SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/dymetrian.db'"""
#config the application to use the required configuration on our configuration class
#app.config.from_object('config.configuration') 
# set the db
db = SQLAlchemy(app)
#manage the migration of the database and the application
"""migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)"""

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


