#!/usr/bin/python3

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/v1/status', methods=['GET'])
def status():
    """ status route handler """
    return jsonify({"status": "OK"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
