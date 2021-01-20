import csv
import datetime

from database import models
from .database import SessionLocal, engine

db = SessionLocal()

models.Base.metadata.create_all(bind=engine)

with open("datafile.csv", "r") as f:
    csv_reader = csv.DictReader(f)

    for row in csv_reader:
        db_user = models.User(
            username = row["username"],
            email = row["email"],
            phoneNumber = row["phoneNumber"],
            password = row["password"],
            created_on = datetime.datetime.strptime(row["create_on", "%Y-%m-%d"],
            )
        db.add(db_user)
        db.commit()
    db.close()


        )