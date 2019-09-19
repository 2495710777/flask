from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '左边画一条龙'

app.run()
