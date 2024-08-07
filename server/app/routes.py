from urllib.parse import urlsplit
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
import sqlalchemy as sa

from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User


@app.route('/')
@app.route('/index')
@login_required
def index() -> str:
    return render_template('index.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login() -> str:
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(sa.select(User).where(
            User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register() -> str:
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/logout')
def logout() -> str:
    logout_user()
    return redirect(url_for('index'))


@app.route('/user/<username>')
@login_required
def user_profile(username: str) -> str:
    user = db.first_or_404(sa.select(User).where(User.username == username))
    return render_template('user.html', user=user)
