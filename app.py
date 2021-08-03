# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 00:47:33 2021
@author: Kushagra
"""

import os
from flask import Flask, flash, request, redirect, render_template,session,make_response
from werkzeug.utils import secure_filename

from flask_sqlalchemy import SQLAlchemy
from flask_cors import cross_origin
from dataBase import Info_table
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.secret_key = "abc123"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/danalitic'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://b3x2mzn3vgxhrr12:kk1wi098ezdx4bdb@tvcpw8tpu4jvgnnq.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/pwjh6mzn4jk2lehc'


#-------------Creating Objects------------#
db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def index():
    
    return render_template('index.html')


@app.route('/submitButton', methods=['GET','POST'])
def submitButton():


    name = request.form.get('name')

    address = request.form.get('add')

    session['userName'] = name

    session['userAddress'] = address

    flag = 'suc'

    entry = Info_table(Name = name, Address = address)
    db.session.add(entry)
    db.session.commit()
    
    return render_template('index.html',Flag = flag)    

@app.route('/infoButton', methods=['GET','POST'])
def infoButton():


    name = session['userName']

    address = session['userAddress']

    flag = 'info'

    return render_template('index.html',flagNew = flag,Name = name,Address = address)


if __name__ == '__main__':
   app.run(debug = False)