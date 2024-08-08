GENDER_API = "https://api.genderize.io?name="
AGE_API = "https://api.agify.io?name="

import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello User !!!" \
           "Type /guess/yourname to give our website a try"


@app.route('/guess/<name>')
def guessing_age_with_gender(name):
    response1 = requests.get(url=f'{AGE_API}{name}')
    your_age = response1.json()["age"]
    response2 = requests.get(url=f'{GENDER_API}{name}')
    your_gender = response2.json()["gender"]
    name = name.title()
    return render_template('guess-age-gender.html', person_name=name, age=your_age, gender=your_gender)


if __name__ == "__main__":
    app.run(debug=True)
