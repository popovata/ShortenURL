"""
The main file where an application starts running
"""

from app import app

if __name__ == "__main__":
    app.debug = True
    app.run()
