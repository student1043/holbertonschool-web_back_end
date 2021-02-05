#!/usr/bin/env python3
""" i18n project """
from flask_babel import babel
from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')


class Config:
    """ Config Class """
    LANGUAGES = ["en", "fr"]
    app.config['BABEL_DEFAULT_LOCALE'] = "en"
    app.config['BABEL_DEFAULT_TIMEZONE'] = "UTC"


@app.route('/')
def home():
    """ i18n project """
    return render_template('1-index.html')
