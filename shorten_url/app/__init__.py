"""
 The file  contains the application factory
"""
from flask import Flask
from app import search


app = Flask(__name__)


from app import routes
