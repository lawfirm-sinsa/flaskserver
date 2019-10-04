from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')

def home():
    return 'hello, world!'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)




