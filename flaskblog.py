from flask import Flask, render_template, url_for
app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug = True)