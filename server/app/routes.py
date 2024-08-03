from flask import render_template

from app import app


@app.route('/')
@app.route('/index')
def index() -> str:
    user = {'username': 'TR33HGR'}
    return render_template('index.html', title='Home', user=user)
