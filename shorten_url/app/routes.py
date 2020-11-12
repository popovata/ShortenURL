""" The file is for view functions than handles requests

"""
from app import app,run
from flask import render_template, request, redirect

WEBSITE_ADDRESS = "http://127.0.0.1:5000/"

@app.route("/", methods=["GET", "POST"])
def home():
    """ Home page of application

    :return: home page of application
    """
    if request.method == "POST":
        url = str(request.form["url"])
        key = run.url_shortener.add_key(url)
        short_url = WEBSITE_ADDRESS + key
        return render_template("index.html",  url=url, result=short_url)
    return render_template("index.html")

@app.route("/<key>")
def redirect_to_website(key):
    """ Redirect user to the right website by short url


    :param key: short url
    :return: the right website
    """
    target_url = run.url_shortener.get_url(key)
    return redirect(target_url)
