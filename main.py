from flask import Flask, render_template
from datafetch import build_table

app = Flask(__name__)


@app.route("/")
def table():
    build_table()
    return render_template("table.html")


if __name__ == "__main__":
    app.run(debug=True)
