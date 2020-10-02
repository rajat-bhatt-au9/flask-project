from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '626faf84b33a1c042a7658c08332f0b3'

# Dummy data

posts = [
    {
        'author' : 'Rajat Bhatt',
        'title' : 'Blog post 1',
        'content' : 'Hi, this is Rajat the awesome creator of websites',
        'date-posted' : 'October 01, 2020'

    }, 
    {
        'author' : 'Shubham Pal',
        'title' : 'Blog post 2',
        'content' : 'Hi, this is Shubham pal the awesome creator of websites',
        'date-posted' : 'April 21, 2018'

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
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'rajatbhatt@gmail.com' and form.password.data == 'qwerty':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessfull, Please check Username and Password', 'danger')

    return render_template('login.html', title='Login', form = form)


if __name__ == "__main__":
    app.run(debug = True)