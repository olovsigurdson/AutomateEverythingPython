from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def home_post():
    first_value = request.form['first_val']
    second_value = request.form['second_val']
    third_value = request.form['third_val']

    volume = float(first_value) * float(second_value) * float(third_value)

    return render_template('index.html', output=volume, firstvalue=first_value, secondvalue=second_value, thirdvalue=third_value)


app.run()

