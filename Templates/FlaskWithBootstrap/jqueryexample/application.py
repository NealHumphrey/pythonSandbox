# -*- coding: utf-8 -*-
"""
    jQuery Example
    ~~~~~~~~~~~~~~

    A simple application that shows how Flask and jQuery get along.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<variable_name>')
def variable_URL(variable_name = None):
    return render_template('index.html', variable_name = variable_name)


#Example pages for calling functions from the page with JQuery
@app.route('/_add_numbers')
def add_numbers():
    """Add two numbers server side, ridiculous but well..."""
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)


@app.route('/adding')
def adding():
    return render_template('adding-example.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0")
