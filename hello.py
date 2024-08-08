from flask import Flask
import random

app = Flask(__name__)


# Extra decorators
def make_bold(function):
    def wrapper_function():
        return f"<b><h1>{function()}<h1></b>"

    return wrapper_function


def make_itallic(function):
    def wrapper_function():
        return f"<em>{function()}</em>"

    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        return f"<u>{function()}</u>"

    return wrapper_function


@app.route('/')  # This @ is a decorator referring to home page
@make_bold
@make_itallic
@make_underlined
def hello_world():
    return "Hello World !!!"


@app.route('/bye')  # Type /bye in the url to refer to the bye page
def bye():
    return "Bye World 😘"


@app.route('/<name>')  # Type /Lincon or any other name and see the magic.
def greet(name):
    return f'Hello {name} Nice to see You Sir !'


# defining a variable in url
@app.route('/<path:username>')  # Type /Lincon/1/2 in the url and it will take the entire path as the username
def greetings(username):
    return f'Hello {username} Good-morning 😃😃😃'


# defining a datatype in the url
@app.route('/<username>/<int:age>')  # Type /Lincon/20 in the url
def greet_with_age(username, age):
    return f"Hi {username} You are {age} years old"


# Special Attribute __main__ used to refer to the top level code of the program in Flask
# __name__ is used to refer to the name of the class or module
# These attribute only run scrips and not the modules
# print(random.__name__)


# This is the main part of the program
if __name__ == "__main__":
    app.run(debug=True)  # Debugger is on, and it automatically reloads the page with changes
