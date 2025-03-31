from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Hej</h1>'


@app.route('/tool')


app.run()