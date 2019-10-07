from flask import Flask, request, jsonify, render_template, url_for
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/lawyer')
def lawyer():
    return render_template('lawyer.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)




