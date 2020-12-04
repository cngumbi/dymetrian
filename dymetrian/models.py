import datetime, re
from dymetrian import db


class AboutContent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    TitleName = db.Column(db.String(100))
    body = db.Column(db.Text)
    created_timestamp = db.Column(db.DateTime, default=datetime.datetime.now)
    modified_timestamp = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)


    def __repr__(self):
        return '<AboutContent: %s>' %self.TitleName