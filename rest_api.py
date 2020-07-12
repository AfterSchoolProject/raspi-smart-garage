from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/action', methods=['POST'])
def action():
    print(request.json['value'])
    return jsonify(status="completed")
