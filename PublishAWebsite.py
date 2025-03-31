from flask import Flask

app = Flask("TheWebsite")

@app.route('/')
def home():
    return "welcome to this website"


@app.route('/andra_delen')
def andra_delen():
    return 'andra delen'


app.run()


