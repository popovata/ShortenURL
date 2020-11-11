"""The file is for view functions than handles requests."""
from app import app, used_keys_and_urls
from flask import render_template, request, redirect

IP_ADDRESS = "http://127.0.0.1:5000/"

@app.route("/", methods=["GET", "POST"])
def home():
    """ Home page of application. не знвю,что писать к таким функциям в коменты"""
    if request.method == "POST":
        url = str(request.form["url"])
        key = used_keys_and_urls.add_key(url)
        result = IP_ADDRESS + key
        return render_template("index.html",  url=url, result=result)
    return render_template("index.html")

@app.route("/<key>")
def redirect_to_website(key):
    link_target = used_keys_and_urls.get_url(key)
    return redirect(link_target)
