"""
Main debugging app starter
"""

from app import app
import os
if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(host='0.0.0.0', debug=True, port=5000)
