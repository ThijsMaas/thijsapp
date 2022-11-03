from flask import Flask, render_template

from .utils import get_data, get_content
from os import environ

app = Flask(__name__)

DB_FILE = environ.get("DB_PATH", "/data/db.txt")

DATA = get_data(DB_FILE)

@app.route("/")
def main():
    today_str, extra_str = get_content(DATA)
    return render_template('index.html', today_str=today_str, extra_str=extra_str)
