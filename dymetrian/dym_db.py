#from flask_sqlalchemy import SQLAlchemy
import re
from datetime import datetime
from sqlalchemy import (MetaData, Table, Column, Integer, Numeric, String, DateTime, ForeignKey, create_engine )
#from dymetrian import db
metadata = MetaData()

users = Table('users', metadata,
    Column('user_id', Integer(), primary_key=True),
    Column('username', String(15), nullable=False, unique=True),
    Column('email_address', String(255), nullable=False),
    Column('phone', String(20), nullable=False),
    Column('password', String(25), nullable=False),
    Column('created_on', DateTime(), default=datetime.now),
    Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
    )

engine = create_engine('sqlite:///dymetrian.db')
metadata.create_all(engine)
"""class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' %self.username
"""
"""import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detct_types = sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
        return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()



def init_db():
    db = get_db()

    with current_app.open_resource('dym_schema.sql') as f :
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    #clear the existing data and create new tables
    init_db()
    click.echo('Initialized the database.')



#register the close_db and the init_db_command with the application instance
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)"""