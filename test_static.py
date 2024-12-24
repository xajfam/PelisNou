from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '<link rel="stylesheet" href="/static/css/style.css">Hello World'

if __name__ == '__main__':
    app.run(debug=True)
