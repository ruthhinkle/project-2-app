from flask import Flask, render_template
from sqlalchemy import create_engine
import requests

engine = create_engine("sqlite:///data.sqlite")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/table")
def table():
    return render_template("table.html")

# 
@app.route("/api/v1.0/station_information")
def station_information():
    url = "https://gbfs.divvybikes.com/gbfs/en/station_information.json"
    engine.execute('INSERT INTO api_logs (url) VALUES (?)', url)
    response = requests.get(url)
    return response.json()

@app.route("/api/v1.0/station_status")
def station_status():
    url = "https://gbfs.divvybikes.com/gbfs/en/station_status.json"
    engine.execute('INSERT INTO api_logs (url) VALUES (?)', url)
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    app.run(debug=True)
