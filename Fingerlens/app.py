from flask import Flask, render_template, request, jsonify
import json
import datetime

app = Flask(__name__)

# Simple in-memory store (you can later replace this with a database)
fingerprints = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', fingerprints=fingerprints)

@app.route('/collect', methods=['POST'])
def collect():
    data = request.get_json()
    data['timestamp'] = datetime.datetime.utcnow().isoformat()
    fingerprints.append(data)
    return jsonify({"status": "success", "data_received": data})

@app.route('/fingerprints')
def view():
    return jsonify(fingerprints)

if __name__ == '__main__':
    app.run(debug=True)
