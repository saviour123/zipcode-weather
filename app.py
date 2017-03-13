from flask import Flask, render_template, request, jsonify, flash
import requests

app = Flask(__name__)

@app.route("/temperature", methods=['POST'])
def temperature():
    zipcode = request.form['zip']
    r = requests.get('http://samples.openweathermap.org/data/2.5/weather?zip=' + zipcode + ',us&appid=44e6bdf7fd7a53e3063deae9ebc94b0c')
    json_object = r.json()
    temp_k = float(json_object["main"]["temp"])
    temp_c = temp_k - 273
    return render_template('temperature.html', temp_k=temp_k, temp_c=temp_c)

@app.route("/")
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

