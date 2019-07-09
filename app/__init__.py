"""
Initializes the app as called from ../debug.py or ../main.py
creates the Flask class as app
"""

from flask import Flask
app = Flask(__name__)
from app import views
