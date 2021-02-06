#!/usr/bin/env python3
""" i18n project """

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext

app = Flask(__name__, template_folder='templates')
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    Config Class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config())


@babel.localeselector
def get_locale():
    """
    get locale language
    """
    if request.url[-2:] in app.config["LANGUAGES"]:
        return request.url[-2:]
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user():
    """
    getting user ID
    """
    UID = request.args.get('login_as')
    if UID and int(UID) in users:
        return users[int(UID)]
    else:
        return None


@app.before_request
def before_request():
    """
    before request
    """
    g.user = get_user()


@app.route('/')
def home():
    """
    i18n project
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
