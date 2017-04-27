from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

form = """
<form action="/testform">
    <input name="q">
    <input type="submit">
</form>
"""


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return form


@app.route('/testform')
def helloform():
    return "This is test form"


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
