"""
The main file where the application starts running
"""

from app import app

if __name__ == "__main__":
    app.debug = True
    app.run()
