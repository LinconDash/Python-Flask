# In this file we will render an entire html file
from flask import Flask, render_template

app = Flask(__name__)
# Always create templates and static directories to save html and css,jpg,png files respectively in the directories


@app.route('/')
def home():
    # return render_template('index.html')
    return render_template('my-site.html')

# Sometimes css doesn't apply to the html files because chrome likes to cache the previous files to avoid usage of the
# internet ,so we have to hard reload the page using Shift+reload button on the webpage
# IMPORTANT : type document.body.contentEditable=true in the console of chrome developer tools to edit the file then
# and there without moving to the inspect section of the file
# We can also delete the elements my clicking on the small icon on the top-left and the clicking the elements on the screen and a backspace


if __name__ == "__main__":
    app.run(debug=True)
