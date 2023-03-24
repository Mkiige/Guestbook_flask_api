# Python REST APIs With Flask, Connexion, and SQLAlchemy – Database Persistence

## Database Persistence

You should first create a virtual environment:

```console
$ python -m venv venv
$ source venv/bin/activate
```

Install the pinned dependencies from `requirements.txt`:

```console
(venv) $ python -m pip install -r requirements.txt
```

Then, navigate into the `Guestbook_flask_api/` folder:

```console
(venv) $ cd Guestbook_flask_api
(venv) $ python app.py
```

To see your home page, visit `http://127.0.0.1:8000`. You can find the Swagger UI API documentation on `http://127.0.0.1:8000/api/ui`.

### Optional: Build the Database

You can build a SQLite database with content by following the commands below.

Navigate inside the `Guestbook_flask_api/`, enter the [Python interactive shell](https://realpython.com/interacting-with-python/) and run the commands below:

```pycon
>>> import sqlite3
>>> conn = sqlite3.connect("people.db")
>>> columns = [
...     "id INTEGER PRIMARY KEY",
...     "lname VARCHAR UNIQUE",
...     "fname VARCHAR",
...     "timestamp DATETIME",
... ]
>>> create_table_cmd = f"CREATE TABLE person ({','.join(columns)})"
>>> conn.execute(create_table_cmd)
>>> people = [
...     "1, 'Fairy', 'Sugar', '2022-10-08 09:15:10'",
...     "2, 'Ruprecht', 'Knecht', '2022-10-08 09:15:13'",
...     "3, 'Bunny', 'Easter', '2022-10-08 09:15:27'",
... ]
>>> for person_data in people:
...     insert_cmd = f"INSERT INTO person VALUES ({person_data})"
...     conn.execute(insert_cmd)
...
<sqlite3.Cursor object at 0x104ac4dc0>
<sqlite3.Cursor object at 0x104ac4f40>
<sqlite3.Cursor object at 0x104ac4fc0>

>>> conn.commit()
```

This will create a database named `people.db` that you can use with your project.

## Author

- **Mary Kiige**, E-mail: [mkiige77@gmail.com]

## License

Distributed under the MIT license. See [`LICENSE`](../LICENSE) for more information.
