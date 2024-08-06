import logging
from logging.handlers import SMTPHandler
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config


def send_errors_over_email() -> None:
    auth: tuple[str, str] = None
    if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
        auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
    secure: tuple[()] = None
    if app.config['MAIL_USE_TLS']:
        secure = ()
    mail_handler = SMTPHandler(
        mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
        fromaddr=f'no-reply@{app.config['MAIL_SERVER']}',
        toaddrs=app.config['ADMINS'],
        subject='App Failure',
        credentials=auth,
        secure=secure)
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

if not app.debug:
    if app.config['MAIL_SERVER']:
        send_errors_over_email()


# pylint: disable=C0413, W0406
from app import routes, models, errors  # noqa: E402, F401
