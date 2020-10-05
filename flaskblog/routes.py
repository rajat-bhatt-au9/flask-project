from flask import Flask, render_template, url_for, flash, redirect
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user


# Dummy data
posts = [
    {
        'author' : 'Rajat Bhatt',
        'title' : 'Blog post 1',
        'content' : 'Hi, this is Rajat the awesome creator of websites.The Paragraphs module allows content creators to choose which kinds of paragraphs they want to place on the page, and the order in which they want to place them. They can do all of this through the familiar node edit screen. There is no need to resort to code, the dreaded block placement config screen or Panelizer overrides. They just use node edit form where all content is available to them in one place. Morpht has taken the Paragraph concept and run with it - building a number of supporting modules giving Paragraphs more base functionality and site builders some easy wins with some Paragraph bundles ready to go.',
        'date-posted' : 'October 01, 2020'

    }, 
    {
        'author' : 'Shubham Pal',
        'title' : 'Blog post 2',
        'content' : 'Hi, this is Shubham pal the awesome creator of websites. The Paragraphs module allows content creators to choose which kinds of paragraphs they want to place on the page, and the order in which they want to place them. They can do all of this through the familiar node edit screen. There is no need to resort to code, the dreaded block placement config screen or Panelizer overrides. They just use node edit form where all content is available to them in one place. Morpht has taken the Paragraph concept and run with it - building a number of supporting modules giving Paragraphs more base functionality and site builders some easy wins with some Paragraph bundles ready to go.',
        'date-posted' : 'April 21, 2018'

    },
    {
        'author' : 'John doe',
        'title' : 'Blog post 3',
        'content' : 'Hi, this is Shubham pal the awesome creator of websites. The Paragraphs module allows content creators to choose which kinds of paragraphs they want to place on the page, and the order in which they want to place them. They can do all of this through the familiar node edit screen. There is no need to resort to code, the dreaded block placement config screen or Panelizer overrides. They just use node edit form where all content is available to them in one place. Morpht has taken the Paragraph concept and run with it - building a number of supporting modules giving Paragraphs more base functionality and site builders some easy wins with some Paragraph bundles ready to go.',
        'date-posted' : 'April 30, 2018'

    }


]



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title = 'About Us')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to Login', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user= User.query.filter_by(email = form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessfull, Please check email and Password', 'danger')

    return render_template('login.html', title='Login', form = form)
