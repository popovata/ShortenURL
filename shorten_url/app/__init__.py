from flask import Flask
from app import search
app = Flask(__name__)

from app import routes

if __name__ == "__main__":
    app.debug = True
    app.run()