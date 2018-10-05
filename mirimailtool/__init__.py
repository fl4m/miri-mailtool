from flask import Flask, render_template, request
from pprint import pformat

from mirimailtool.util import filter_addresses

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/', methods=['GET'])
    def index():
        """Renders the index template which displays the input forms."""
        return render_template('index.html')
        
    @app.route('/', methods=['POST'])
    def result():
        """Filters the submitted addresses and displays the result."""
        old = request.form['old-addr']
        new = request.form['new-addr']

        addrs, stats = filter_addresses(old, new)
            
        return render_template('result.html', addrs=addrs, stats=stats)
        
    return app