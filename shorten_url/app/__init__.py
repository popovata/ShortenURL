from flask import Flask
from app import search

SHORT_KEY_LENGTH = 5
app = Flask(__name__)
used_keys_and_urls = search.KeyToUrl(SHORT_KEY_LENGTH)

from app import routes
