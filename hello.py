from flask import Flask, render_template, request
from pprint import pformat

from mailtool import filter_addresses

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    """Renders the index template which displays the input forms."""
    return render_template('index.html')
    
@app.route('/', methods=['POST'])
def hello():
    """Filters the submitted addresses and displays the result."""
    old = request.form['old-addr']
    new = request.form['new-addr']

    addrs = filter_addresses(new, old)
    if addrs is None:
        addrs = set()
        
    return pformat(addrs, indent=4)
    
    