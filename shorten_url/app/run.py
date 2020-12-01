"""
The main file starts to run the application.
"""

from app import app

if __name__ == "__main__":
    app.debug = True
    app.run()
