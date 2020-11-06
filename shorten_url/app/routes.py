"""A file for view functions."""
from app import app
from app import search
from flask import Flask, render_template, request


@app.route("/", methods=["GET", "POST"])
def result():
    if request.method == "POST":
        url = request.form["url"]
        new_db = search.ShortKeys()
        results = new_db.add_key(str(url))
        return render_template("index.html", results=results)
    return render_template("index.html")
