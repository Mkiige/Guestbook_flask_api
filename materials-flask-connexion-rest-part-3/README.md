# Python REST APIs With Flask, Connexion, and SQLAlchemy – Database relation

## Real Python Flask REST API – Database relation

You should first create a virtual environment:

```console
$ python -m venv venv
$ source venv/bin/activate
```

Install the pinned dependencies from `requirements.txt`:

```console
(venv) $ python -m pip install -r requirements.txt
```

Then, navigate into the `Guestbook/` folder:

```console
(venv) $ cd Guestbook_flask_api
(venv) $ python app.py
```

To see your home page, visit `http://127.0.0.1:8000`. You can find the Swagger UI API documentation on `http://127.0.0.1:8000/api/ui`.

### Optional: Build the Database

You can build a SQLite database with content by following the commands below.

Navigate into the `Guestbook_flask_api/` folder:

```console
(venv) $ python build_database.py
```

This will delete any existing database and create a new database named `people.db` that you can use with your project.

## Author

- **Mary Kiige**, E-mail: [mkiige77@gmail.com]

## License

Distributed under the MIT license. See [`LICENSE`](../LICENSE) for more information.
