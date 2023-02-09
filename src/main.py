from flask import Flask
from datetime import date

app = Flask(__name__)


@app.route('/')
def is_it_friday_yet():
    return "It is friday !" if date.today().isoweekday() == 5 else "It's not friday yet :("
