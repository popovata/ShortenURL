"""
The main file where an application starts running
"""

from app import app

SHORT_KEY_LENGTH = 5

if __name__ == "__main__":
    app.debug = True
    app.run()