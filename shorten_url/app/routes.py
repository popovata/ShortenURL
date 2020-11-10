"""A file for view functions."""
from app import app
from app import search
from flask import Flask, render_template, request, redirect

SHORT_KEY_LENGTH = 5

new_db = search.ShortKeys(SHORT_KEY_LENGTH)


@app.route("/", methods=["GET", "POST"])
def result():
    if request.method == "POST":
        url = request.form["url"]
        url = str(url)
        result = "http://127.0.0.1:5000/" + new_db.add_key(url)
        return render_template("index.html",  url=url, result=result)
    return render_template("index.html")

@app.route("/<result>")
def expand_to_long_url(result):
    link_target = new_db.get_url(result)
    print(link_target)
    return redirect(link_target)
