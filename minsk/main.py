from flask import Flask, render_template, jsonify
from flask_cors import CORS
import random
import time

app = Flask(__name__)
CORS(app)


# Симуляция GPS-данных
def generate_gps_data():
    latitude = 53.9045 + random.uniform(-0.05, 0.05)
    longitude = 27.5590 + random.uniform(-0.05, 0.05)
    return {'latitude': latitude, 'longitude': longitude}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/gps_data')
def gps_data():
    # Симулируем задержку для обновления данных
    time.sleep(1)  # 1 секунда задержки
    data = generate_gps_data()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
