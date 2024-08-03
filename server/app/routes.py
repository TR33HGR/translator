from flask import flash, redirect, render_template

from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index() -> str:
    user = {'username': 'TR33HGR'}
    return render_template('index.html', title='Home', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login() -> str:
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login request user {form.username.data}, remember me={
              form.remember_me.data}')
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
