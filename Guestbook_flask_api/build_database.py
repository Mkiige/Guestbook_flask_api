from datetime import datetime

from config import app, db
from models import Note, Person

PEOPLE_NOTES = [
    {
        "lname": "Fairy",
        "fname": "Tooth",
        "notes": [
            ("I brush my teeth after each meal.", "2023-03-27 14:50:24"),
            (
                "The other day a friend said, I have big teeth.",
                "2023-03-27 14:50:54",
            ),
            ("Do you pay per gram?", "2023-03-27 14:51:10"),
        ],
    },
    {
        "lname": "Ruprecht",
        "fname": "Knecht",
        "notes": [
            (
                "I swear, I'll do better this year.",
                "2023-03-27 14:51:15",
            ),
            (
                "Really! Only good deeds from now on!",
                "2023-03-27 14:52:21",
            ),
        ],
    },
    {
        "lname": "Bunny",
        "fname": "Easter",
        "notes": [
            (
                "Please keep the current inflation rate in mind!",
                "2023-03-27 14:52:54",
            ),
            ("No need to hide the eggs this time.", "2023-03-27 14:53:17"),
        ],
    },
]

with app.app_context():
    db.drop_all()
    db.create_all()
    for data in PEOPLE_NOTES:
        new_person = Person(lname=data.get("lname"), fname=data.get("fname"))
        for content, timestamp in data.get("notes", []):
            new_person.notes.append(
                Note(
                    content=content,
                    timestamp=datetime.strptime(
                        timestamp, "%Y-%m-%d %H:%M:%S"
                    ),
                )
            )
        db.session.add(new_person)
    db.session.commit()
