# app.py
#This is a simple Python Flask web application that defines a route for the root URL path ("/"). 
#The route function returns the result of calling the render_template function, which renders a Jinja2 template called "home.html". 
#The __name__ == "__main__" condition ensures that the server only runs when the script is executed directly (as opposed to when it is imported as a module).

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
