from flask import Flask, render_template, request, redirect, url_for
import os
import csv
from datetime import datetime
from matplotlib import pyplot as plt
import numpy as np
import json


app = Flask(__name__)

# Define the path to your CSV file
data_file = "/workspaces/76244869/app_track/drives.csv"



# Check if the CSV file exists; if not, create it
if not os.path.exists(data_file):
    with open(data_file, "w", newline="") as csvfile:
        fieldnames = ["id","date", "driver"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()




@app.route("/")
def index():
    # Load existing data from CSV
    Leo = []
    Anthony = []


    with open(data_file, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        drives = []
        for row in reader:
            drives.append(row)
            print(row)

            if row["driver"] == "Leo":
                Leo.append(int(1))
                print(Leo)

            elif row["driver"] == "Anthony":
                Anthony.append(int(1))
                print(Anthony)

    x = sum(Anthony)
    y = sum(Leo)
    x_y = [x, y]
    sum_drive = json.dumps(x_y)
    Drivers = ["Leo", "Anthony"]

    return render_template("index.html", drives = drives, sum_drive = sum_drive, Drivers = Drivers)

@app.route("/add_drive", methods=["POST"])
def add_drive():
    # Add a new drive entry to the CSV file
    date = datetime.now().strftime("%Y-%m-%d")
    driver = request.form.get("driver")

    with open(data_file) as f:
         id = sum(1 for line in f)


    with open(data_file, "a", newline="") as csvfile:
        fieldnames = ["id", "date", "driver"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({"id": id, "date": date, "driver": driver})

    return redirect(url_for("index"))


@app.route("/delete_drive", methods=["POST"])
def delete_drive():

    # Delete row from the CSV file
    drives = []
    id = request.form.get("id")
    drives.clear()

    with open(data_file, newline="") as csvfile:
        file = csv.DictReader(csvfile)
        for row in file:
            if row["id"] != str(id):
                drives.append(row)
                fieldnames = row
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            else:
                continue


    return render_template("index.html", drives=drives)




if __name__ == "__main__":
    app.run(debug=True)
