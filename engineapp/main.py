from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from link_provider import ShortLink
app = Flask(__name__)
app.debug = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def create_link():
    return render_template('create_link.html')

@app.route('/generate_link', methods=['GET', 'POST'])
def generate_link():
    url = request.form['url']
    if url == "" or url.isspace():
        return "Please enter a URL"
    link = ShortLink.generate_link(url)
    return '<a href="' + link + '">' + link + '</a>'

@app.route('/<shorturl>')
def redirect_link(shorturl):
    link = ShortLink.get_link(shorturl)
    return redirect(link, code=302)


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
