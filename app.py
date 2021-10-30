import random

from flask import Flask,render_template, url_for, session, make_response, request, redirect
import sqlite3
import requests


from datetime import datetime
from flask import escape
import uuid
import os
import time


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/get_data",methods = ['POST','GET'])
@app.route('/get_data/<int:quan>',methods = ['POST','GET'])
def info(quan = 1):
    result = {}
    users_uuid = []
    date_of_request = []
    time_of_response = []
    if request.method == 'GET':
        for i in range(quan):
            date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            date_millsec = datetime.now().strftime('%f')

            users_uuid.append(uuid.uuid4())
            date_of_request.append(date)
            finish = int(datetime.now().strftime('%f')) - int(date_millsec)
            time_of_response.append(finish)

        result['UUID'] = users_uuid
        result['Date of request'] = date_of_request
        result['Time of response'] = time_of_response

        return result








