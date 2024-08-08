from flask import Flask, render_template
import random
import datetime
import requests
app = Flask(__name__)

# we used a simple jinja in the index.html
@app.route('/')
def home():
    current_year = datetime.datetime.now().year
    random_number = random.randint(1, 10)
    return render_template('index.html', num=random_number, year=current_year)

# We used a multiline jinja in the blog.html file
@app.route('/blog/<int:num>')
def show_blogs(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts, given_id=num)

if __name__ == "__main__":
    app.run(debug=True)
