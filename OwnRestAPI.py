from flask import Flask, jsonify
from BScurrencyconverter import get_currency

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>TEST</h1> <p>Example URL: /api/v1/usd-eur</p>'


@app.route('/api/v1/<in_curr>-<out_curr>')
def api(in_curr, out_curr):
    currency = get_currency(in_curr, out_curr)
    data = {
        "input_currency": in_curr,
        "outut_currency": out_curr,
        "rate": currency
    }
    #Flask-funktion som gör datat till json
    return jsonify(data)


@app.route('/api/v1/thehorror')
def api2():
    return 'The horror...'


app.run()

