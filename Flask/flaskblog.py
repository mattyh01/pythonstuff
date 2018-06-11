from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite//site.db'
db = SQLAlchemy(app)

#DB info here

class User(db.Model):
    id = db.column(db.Integer, primary key)
    username = db.column(db.String(20), unique=True, nullable=False)
    email = db.column(db.String(120), unique=True, nullable=False)
    image_file = db.column(db.String(20)) nullable=False, default='default.jpg')
    password = db.column(db.String(60)), nullable=False)

#Repr how the object is printed out

    def __repr__(self):
        return f"User('{self.username}'), '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.column(db.Integer, primary key)
    title = db.column(db.String(100), nullable=False)
    date = db.column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.column(db.Text, nullable=False)

def __repr__(self):
    return f"Post('{self.title}'), '{self.date_posted}')"



posts = [
    {
        'author': 'Matt Holmes',
        'title': 'Post 1',
        'content': 'First post content',
        'date_posted': '30th May, 2018'
    },
    {
        'author': 'Amy Herbert',
        'title': 'Post 2',
        'content': 'Second post content',
        'date_posted': '31st May, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    app.run(debug=True)
