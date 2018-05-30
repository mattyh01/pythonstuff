from flask import Flask, flash, redirect, render_template, session, abort, url_for
from forms import RegistrationForm, LoginForm #Imports the class

app = Flask(__name__) #Name is name of the module

app.config['SECRET_KEY'] = 'abCDSeSdvFvsrfaFunSgIGv'



posts = [
    {
        'author': 'Matthew Holmes',
        'title': 'First Post',
        'content': 'First comment'

    },
    {
        'author': 'Test User',
        'title': 'Second Post',
        'content': 'Second comment'

    }


]


@app.route("/home")
def home():
    return render_template(
        'home.html', posts=posts)

@app.route("/Register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!')
    return render_template(
        'register.html', title='Register', form=form)

@app.route("/Login")
def login():
    form = LoginForm()
    return render_template(
        'login.html', title='Login', form=form)


#Different routes below as defined
#by the decorator @app.route()

#Index Page (Needs work)

@app.route("/index")
def index():
    return render_template(
        'index.html')


@app.route("/about")
def about():
    return render_template(
        'about.html', title='- About me')


@app.route("/championships/<string:name>/")
def championships(name):
    return render_template(
        'flask.html', name=name)




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
