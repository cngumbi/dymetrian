import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager


app = Flask(__name__)

app.config['SECRET_KEY'] = '&\xfb?\xfbL\xd7\xc0z\x19ewF\xdd\xe6\xce(M\xbc\x15,'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s/dymetrian.db'
# set the db
db = SQLAlchemy(app)
#manage the migration of the database and the application
"""migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)"""

from dymetrian import routes

