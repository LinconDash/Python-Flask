from flask import Flask

app = Flask(__name__)


# Flask can render html and css tags simply
@app.route('/')
def hello_world():
    return "<h1 style='text-align: center'>Hello World !!!</h1>" \
           "<p>This is a paragraph</p>" \
           "<img src='https://i0.wp.com/www.printmag.com/wp-content/uploads/2021/02/4cbe8d_f1ed2800a49649848102c68fc5a66e53mv2.gif?fit=476%2C280&ssl=1'>"


if __name__ == "__main__":
    app.run(debug=True)
