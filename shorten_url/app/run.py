"""
The main file where an application starts running
"""

from app import app, search

SHORT_KEY_LENGTH = 5

if __name__ == "__main__":
    app.debug = True
    #url_shortener = search.KeyToUrl(SHORT_KEY_LENGTH)
    app.run()