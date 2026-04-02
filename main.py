from flask import Flask, render_template, request, session, flash
from flask_session import Session
import os

app = Flask(__name__)

app.config['SESSION_PERMANENT'] = True
app.config['SESSION_TYPE'] = "filesystem"

Session(app)

file_save_location = "static/images"

@app.route('/')
def homePage():
    

@app.route('/ItemCollection'):
    def displayItems():
    

@app.route('/addItem', methods=['POST']):
    def 

@app.route('/removeItems'):
   def 