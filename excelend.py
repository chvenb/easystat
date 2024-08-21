import pandas as pd
from flask import Flask,request,redirect,render_template,url_for

import os


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED EXTENSIONS'] = {'xlsx,xls'}


def allowed_filetype(filename):
    spiti = filename.split('.')
    if spiti.lower() in app.config['ALLOWED EXTENSIONS']:
        return 1
    else:
        return -1
    




