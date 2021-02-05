#!/usr/bin/env python3
""" i18n project """
from flask_babel import Babel
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


@babel.localeselector
def get_locale():
    """ get locale language"""
    return request.accept_languages.best_match(['fr', 'en'])

babel = Babel(app)

@app.route('/')
def home():
    """ i18n project """
    return render_template('2-index.html')
