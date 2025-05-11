from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log():
    data = request.json
    with open("data.txt", "a") as f:
        f.write(f"{datetime.now()} | {data}\n")
    return {"status": "success"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)