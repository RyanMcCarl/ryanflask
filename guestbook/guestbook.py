#!/usr/env/python3
#
# -*- coding: utf-8 -*-
# guestbook.py
#
#

from flask import Flask, render_template

# Instantiate app
app = Flask(__name__)

# Create a route, i.e. place I can type in browser to place HTTP request.
# The request runs the code associated with that route.
# app.route(endpoint) = decorator
# Under decorator, create a view function

@app.route('/')
def index():
    return '<h1>Hello!</h1>'

# Can pass in arguments in the endpoint in the address bar.
# e.g.: http://localhost:5000/home/Denver
@app.route('/<place>')
def place(place):
    return '<h1>You are on the ' + place + ' page!</h1>'

# Can put different methods in URL. Anything sent in address bar = a GET request.
# By default, endpoints include implicit parameter `methods=['GET']`.
# But if include 'POST', must also include 'GET'.
@app.route('/home', methods=['GET', 'POST'])
def home():
    links = {'Ryan McCarl':'http://ryanmccarl.com', 'WordBrewery':'https://wordbrewery.com'}
    return render_template('home.html', links=links) #myvar='Flask example')

# This returns a template rather than inline html. Templates must be in /templates folder.
@app.route('/csspractice', methods=['GET', 'POST'])
def csspractice():
    links = {'Ryan McCarl':'http://ryanmccarl.com', 'WordBrewery':'https://wordbrewery.com'}
    return render_template('csspractice.html') #myvar='Flask example')

# Debug = watch mode
if __name__ == '__main__':
    app.run(debug=True)

    render