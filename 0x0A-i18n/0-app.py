#!/usr/bin/env python3
""" i18n project """
from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')


@app.route('/')
def home():
    """ i18n project """
    return render_template('0-index.html')
