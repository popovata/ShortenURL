from app import app
from app import search
from flask import Flask, render_template, request

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        # get url that the user has entered
        url = request.form['url']
            #r = requests.get(url)
    #new_db = search.shortened_url_db()
    #results = new_db.add_url(url)
    return render_template('index.html', results="nya")
