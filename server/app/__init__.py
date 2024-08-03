from flask import Flask

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# pylint: disable=C0413
from app import routes  # noqa: E402, F401
