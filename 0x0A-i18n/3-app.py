#!/usr/bin/env python3
""" i18n project """
from flask_babel import Babel, gettext, ngettext
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


class Config:
    """ Config Class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


babel = Babel(app)
app.config.from_object(Config())


@babel.localeselector
def get_locale():
    """ get locale language"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def home():
    """ i18n project """
    return render_template('2-index.html')
