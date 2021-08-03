from threading import Event
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/danalitic'
 

db = SQLAlchemy(app)


 #----DATABASE START----#
class Info_table(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    Text = db.Column(db.Text, nullable=False)
    Address = db.Column(db.Text, nullable=False)
    

    