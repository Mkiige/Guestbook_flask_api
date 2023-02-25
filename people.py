# This code defines a basic REST API with four functions to perform CRUD (Create, Read, Update, Delete) operations on a dictionary of people objects

from datetime import datetime

from flask import abort, make_response


#The get_timestamp() function returns the current date and time as a formatted string.
def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# The PEOPLE dictionary contains three sample people objects, each with a first name, last name, and timestamp.
PEOPLE = {
    "Fairy": {
        "fname": "Tooth",
        "lname": "Fairy",
        "timestamp": get_timestamp(),
    },
    "Ruprecht": {
        "fname": "Knecht",
        "lname": "Ruprecht",
        "timestamp": get_timestamp(),
    },
    "Bunny": {
        "fname": "Easter",
        "lname": "Bunny",
        "timestamp": get_timestamp(),
    },
}


# The read_all() function returns a list of all the people objects in the PEOPLE dictionary.
def read_all():
    return list(PEOPLE.values())


# The create(person) function creates a new person object with a given first and last name and adds it to the PEOPLE dictionary.
# If a person with the same last name already exists, it returns an HTTP 406 error.
def create(person):
    lname = person.get("lname")
    fname = person.get("fname", "")

    if lname and lname not in PEOPLE:
        PEOPLE[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp(),
        }
        return PEOPLE[lname], 201
    else:
        abort(406, f"Person with last name {lname} already exists")


# The read_one(lname) function returns a single person object from the PEOPLE dictionary by their last name.
# If the person does not exist, it returns an HTTP 404 error.
def read_one(lname):
    if lname in PEOPLE:
        return PEOPLE[lname]
    else:
        abort(404, f"Person with last name {lname} not found")


# The update(lname, person) function updates a person object in the PEOPLE dictionary by their last name with a given first name and updates the timestamp. 
# If the person does not exist, it returns an HTTP 404 error.       
def update(lname, person):
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname", PEOPLE[lname]["fname"])
        PEOPLE[lname]["timestamp"] = get_timestamp()
        return PEOPLE[lname]
    else:
        abort(404, f"Person with last name {lname} not found")


# The delete(lname) function deletes a person object from the PEOPLE dictionary by their last name.
# If the person does not exist, it returns an HTTP 404 error.        
def delete(lname):
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(f"{lname} successfully deleted", 200)
    else:
        abort(404, f"Person with last name {lname} not found")
