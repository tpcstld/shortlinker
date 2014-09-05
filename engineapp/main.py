from flask import Flask
from flask import render_template
app = Flask(__name__)
app.debug = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def create_link():
    return render_template('create_link.html')

@app.route('/generate_link', methods=['GET', 'POST']t)
def generate_link():
    return "Hello, World!"


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
