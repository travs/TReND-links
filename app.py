from flask import (Flask, g, render_template, flash, redirect, url_for,
                  abort)
from flask.ext.bcrypt import check_password_hash
from flask.ext.login import (LoginManager, login_user, logout_user,
                             login_required, current_user)

import forms
import models

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = 'auoesh.bouoastuh.43,uoausoehuosth3ououea.auoub!'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None


@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()
    g.user = current_user


@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response

@app.route('/user/<nickname>')
def user_profile(nickname):
    user = models.User.get(models.User.nickname == nickname)
    if not user:
        flash('User could not be found.')
    else:
        profile = models.UserProfile.get(models.UserProfile.user == user)
    return render_template(
        'user-profile.html', 
        profile=profile,
        user=user)

@app.route('/register', methods=('GET', 'POST'))
def register():
    form = forms.RegistrationForm()
    if form.validate_on_submit():
        flash('Yay! You registered.', 'success')
        models.User.create_user(
            email=form.email.data,
            password=form.password.data)
        return redirect(url_for('index'))
    return render_template('register.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You've been logged out.", 'success')
    return redirect(url_for('index'))

@app.route('/members')
def members():
    user_data = models.User.select().where(models.User.confirmed == True)
    print(user_data)
    return render_template('members.html', rows=user_data)

@app.route('/', methods=('GET', 'POST'))
def index():
    print(current_user)
    login_form = forms.LoginForm()
    if login_form.validate_on_submit():
        try:
            user = models.User.get(models.User.email == login_form.email.data)
        except models.DoesNotExist:
            flash("Your email or password doesn't match.", 'error')
        else:
            if check_password_hash(user.password, login_form.password.data):
                login_user(user)
                print(current_user)
                flash("You've been successfully logged in!", 'success')
                return redirect(url_for('index'))
            else:
                flash("Your email or password doesn't match.", 'error')
    return render_template('index.html', form=login_form)

if __name__ == '__main__':
    models.initialize()
    try:
        models.User.create_user(
            email='kenneth@teamtreehouse.com',
            password='password',
            admin=True
        )
    except ValueError:
        pass
    app.run(debug=DEBUG, host=HOST, port=PORT)
