from flask import Flask, render_template

from .utils import get_data, get_content


DATA = get_data("/data/db.txt")

app = Flask(__name__)

@app.route("/")
def main():
    today_str, extra_str = get_content(DATA)
    return render_template('index.html', today_str=today_str, extra_str=extra_str)
