from typing import Any
import sqlalchemy as sa
import sqlalchemy.orm as so

# pylint: disable=W0611
from app import app, db  # noqa: F401
from app.models import User


@app.shell_context_processor
def make_shell_context() -> dict[str, Any]:
    return {'sa': sa, 'so': so, 'db': db, 'User': User}
