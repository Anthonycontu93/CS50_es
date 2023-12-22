import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")





@app.after_request
def after_request(response):

    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"

    return response


@app.route("/", methods=["GET","POST"])
def index():



    if request.method == "GET":

        #Todo: Display the entries in the database on index.html
        entries = db.execute("SELECT * FROM birthdays")
        return render_template("index.html", entries = entries)



@app.route("/deregister", methods=["GET","POST"])
def deregister():

    # delete registrant

    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM birthdays WHERE id = ?", id)
    return redirect("/")


@app.route("/insert", methods=["GET","POST"])
def insert():


    # Todo: Add the user's entry into the database

    if request.method == "POST":

            name = request.form.get("name")
            month = request.form.get("month")
            day = request.form.get("day")

            db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)

            return redirect("/")


@app.route("/modify", methods=["GET","POST"])
def modify():


    # modify registrant

    if request.method == "POST":

            name = request.form.get("name")
            month = request.form.get("month")
            day = request.form.get("day")
            id = request.form.get("id")

            db.execute("UPDATE birthdays SET month = ?, day = ? WHERE id = ? ",  month, day, id)

            return redirect("/")












