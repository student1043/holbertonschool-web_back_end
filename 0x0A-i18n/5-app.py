#!/usr/bin/env python3
"""
Task 5 of i18n project, making user login and changing
the method of request
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    Config Class for languages and timezones!
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config())


@babel.localeselector
def get_locale():
    """
    get locale language from request URL, might change this later
    """
    if request.url[-2:] in app.config["LANGUAGES"]:
        return request.url[-2:]
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user():
    """
    getting user ID through request.args.get and returning it
    """
    UID = request.args.get('login_as')
    if UID and int(UID) in users:
        return users[int(UID)]
    else:
        return None


@app.before_request
def before_request():
    """
    before request that sets the g.user to the function we made get_user
    """
    g.user = get_user()


@app.route('/')
def home():
    """
    the main function of our app this should be updated with the latest
    index file
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
