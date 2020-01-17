from flask import Flask, render_template, request
from pprint import pformat
import os

from mirimailtool.util import filter_addresses, union_addresses


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    # configuration
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/', methods=['GET'])
    def index():
        """Renders the index template which displays the input forms."""
        return render_template('index.html')
        
    @app.route('/', methods=['POST'])
    def result():
        """Filters the submitted addresses and displays the result."""
        old = request.form['old-addr']
        new = request.form['new-addr']

        #addrs, stats = filter_addresses(old, new)
        addrs, stats = union_addresses(old, new)

        return render_template('result.html', addrs=addrs, stats=stats)
        
    return app