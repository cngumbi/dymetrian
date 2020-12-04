from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager


#custome modules
from config import Configuration


app = Flask(__name__)
#config the application to use the required configuration on our configuration class
app.config.from_object('config.configuration') 
# set the db
db = SQLAlchemy(app)