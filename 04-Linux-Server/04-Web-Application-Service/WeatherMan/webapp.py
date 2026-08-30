from flask import Flask, render_template, request
from waitress import serve
from weather_client import get_forecast_data as data

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/results")
def load_forecast():
    location = request.args.get("location").strip() or "new york city"
    forecast = data(location)

    return render_template("results.html", **forecast)


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
