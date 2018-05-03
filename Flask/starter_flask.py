from flask import Flask, flash, redirect, render_template, session, abort
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

#Different routes below as defined
#by the decorator @app.route()

@app.route("/aboutme")
def aboutme():
    return "About me page"

#@app.route("/championships/<string:name>/")
#def championships(name):
#    return render_template(
#        'test.html', name=name)




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
