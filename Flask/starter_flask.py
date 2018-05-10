from flask import Flask, flash, redirect, render_template, session, abort
app = Flask(__name__) #Name is name of the module

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
    return "<h1>Hello home page!</h1>"

#Different routes below as defined
#by the decorator @app.route()

#Index Page (Needs work)

@app.route("/index")
def index():
    return render_template(
        'index.html')

@app.route("/blogs")
def blog():
    return render_template(
        'blog.html', posts=posts)

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
