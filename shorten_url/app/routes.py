"""
The file is for view functions that handle requests
"""
from app import app, search
from flask import render_template, request, redirect
import urlparse


@app.route("/", methods=["GET", "POST"])
def home():
    """
    Home page of the application

    :return: home page of the application
    """
    if request.method != "POST":
        return render_template("index.html")
    base_url = str(request.form["url"])
    url_shortener = search.KeyToUrl()
    key = url_shortener.add_key(base_url)
    website_address = str(request.url_root)
    short_url = urlparse.urljoin(website_address, '/' + key)
    return render_template("index.html", url=base_url, short_url=short_url)


@app.route("/<key>")
def redirect_to_website(key):
    """
    Redirect a user to the right website by short URL

    :param key: short url
    :return: the right website
    """
    url_shortener = search.KeyToUrl()
    target_url = str(request.url_root)
    try:
        target_url = url_shortener.get_url(key)
    except RuntimeError:
        print("unknown key: ", key)
    return redirect(target_url)
