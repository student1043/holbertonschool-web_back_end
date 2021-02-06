#!/usr/bin/env python3
"""
Task 5 of i18n project, making user login and changing
the method of request
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
import pytz


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
    UID = request.args.get('login_as')
    pref = request.args.get('locale')
    if (pref is not None and pref in app.config["LANGUAGES"]):
        return pref
    if (UID is not None and users[int(UID)]['locale'] is not None
            and users[int(UID)]['locale'] in app.config["LANGUAGES"]):
        return users[int(UID)]['locale']
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@babel.timezoneselector
def get_timezone():
    """
    get locale timezone from URL and user settings
    """
    UID = request.args.get('login_as')
    mytimezone = request.args.get('timezone')
    try:
        if mytimezone is not None and mytimezone in pytz.timezone:
            return mytimezone
        if (UID is not None and users[int(UID)]['timezone'] is not None
                and users[int(UID)]['timezone'] in pytz.timezone):
            return users[int(UID)]['timezone']
        return pytz.timezone('UTC')
    except pytz.exceptions.UnknownTimeZoneError:
        return
    return app.config["BABEL_DEFAULT_TIMEZONE"]


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
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run()
