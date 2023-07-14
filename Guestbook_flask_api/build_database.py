from datetime import datetime
from config import app, db
from models import Note, Person

PEOPLE_NOTES = [
    {
        "lname": "Zeddy",
        "fname": "Cherry",
        "notes": [
            ("Pool party at mines.", "2023-07-14 17:10:24"),
            (
                "How about a roadtrip next month?.",
                "2023-07-14 22:17:54",
            ),
            ("Do you pay love hiking?", "2023-03-26 22:18:10"),
        ],
    },
    {
        "lname": "Raph",
        "fname": "Kim",
        "notes": [
            (
                "I swear, I'll get it done.",
                "2023-07-15 09:15:03",
            ),
            (
                "Website done!",
                "2023-07-14 13:09:21",
            ),
        ],
    },
    {
        "lname": "Ree",
        "fname": "Sab",
        "notes": [
            (
                "Remember the email!",
                "2023-07-16 22:47:54",
            ),
            ("No need to hide the eggs this time.", "2023-07-16 13:03:17"),
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
