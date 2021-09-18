from app import app

@app.route('/')
@app.route('/index')
def index():
    """
    a function that defines the route index
    """
    return "<h1> hello world </h1>"