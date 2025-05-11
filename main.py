from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

# Data storage file
LOG_FILE = "data.txt"

@app.route('/log', methods=['POST'])
def log():
    data = request.json
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} | {data}\n")
    return jsonify({"status": "success"})

# 👇 ADD THIS NEW ROUTE 👇
@app.route('/view')
def view_logs():
    if not os.path.exists(LOG_FILE):
        return "No data collected yet!"
    with open(LOG_FILE, "r") as f:
        return f"<pre>{f.read()}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
