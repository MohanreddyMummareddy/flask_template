from flask import url_for, render_template, session, request, redirect, g
from app import app, scripts
"""
Main routing file for app
"""
#main home url 
@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')
#backups route for just backups with data from scripts from home file
@app.route('/path', methods=['GET'])
def backups():
    return render_template('template.html',head="Backups")
