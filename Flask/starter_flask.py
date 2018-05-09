from flask import Flask, flash, redirect, render_template, session, abort
app = Flask(__name__) #Name is name of the module

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

#Different routes below as defined
#by the decorator @app.route()

#Index Page (Needs work)

@app.route("/index")
def index():
    return render_template(
        'index.html')

@app.route("/aboutme")
def aboutme():
    return "About me page"

@app.route("/championships/<string:name>/")
def championships(name):
    return render_template(
        'flask.html', name=name)




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
