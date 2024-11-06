#!/usr/bin/python3
""" This flask implementation returns id a number is
passed"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnh():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def C(text):
    return "C {}".format(text.replace("_"," "))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>',strict_slashes=False)
def python(text="is cool"):
    return "Python {}".format(text.replace("_", " "))

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return "{:d} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n: int):
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n: int):
    is_even = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', n=n, is_even=is_even)

@app.route('/states_list', strict_slashes=False)
def show_the_states():
    """ Function that displays a HTML page that displays aall states created"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown(exception):
    """removes current SQLAlchemy Session"""
    storage.close()

@app.route('/states', strict_slashes=False)
def cities_by_states():
    """
    Display a HTML page with a list of all State objects and their respective City objects sorted by name.
    """
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)

@app.route('/states/<id>', strict_slashes=False)
def states_cities(id):
    """
    Display a HTML page with a list of City objects linked to the State sorted by name.
    """
    state = storage.get(State, id)

    cities = sorted(state.cities, key=lambda city: city.name)
    return render_template('9-states.html', state=state, cities=cities)

if __name__ == '__main__' :
    app.run(host='0.0.0.0', port=5000)
