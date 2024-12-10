from flask import Flask, jsonify
import requests

app = Flask(__name__)
API_URL = "https://catfact.ninja/fact"

@app.route('/', methods=['GET'])
def get_random_cat_fact():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json(), 200
    
    return jsonify({"error": "Unable to fetch cat fact :<"}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
