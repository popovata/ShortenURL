""" The file is for view functions than handles requests

"""
from app import app, search, run
from flask import render_template, request, redirect
import urlparse

@app.route("/", methods=["GET", "POST"])
def home():
    """ Home page of application

    :return: home page of application
    """
    if request.method == "POST":
        base_url = str(request.form["url"])
        url_shortener = search.KeyToUrl(run.SHORT_KEY_LENGTH)
        key = url_shortener.add_key(base_url)
        url = '/' + key
        website_address = str(request.url_root)
        res = urlparse.urljoin(website_address, url)
        return render_template("index.html",  url=base_url, result=res)
    return render_template("index.html")

@app.route("/<key>")
def redirect_to_website(key):
    """ Redirect user to the right website by short url


    :param key: short url
    :return: the right website
    """
    url_shortener = search.KeyToUrl(run.SHORT_KEY_LENGTH)
    target_url = url_shortener.get_url(key)
    return redirect(target_url)
