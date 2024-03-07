from flask import Flask, render_template


# creating a flask instance
app = Flask(__name__)

# creating a route decorator
@app.route('/')
def index():
    first_name = "mcodex"
    return render_template('index.html', first_name=first_name)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)



# custom error pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# custom error pages
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

