#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
from flask import jsonify

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

warrior= [{
    "name": "Black Panther",
    "realName": "T\'Challa",
    "since": 1966,
    "powers": [
        "superhuman strength",
        "Genius-level intellect",
        "expert hand to hand combattant",
        "highly proficient tactician"
              ]
             }]

@app.route("/")
def wakanda():
    # jsonify returns legal JSON
    return jsonify(warrior)


@app.route("/html")
def hello_world():
   return render_template('helloname.html', name= "Hermanator")

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE

