from flask import Flask, request, jsonify, render_template, url_for, redirect, session
import requests

from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client.dbLFD

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/lawyer')
def lawyer():
    return render_template('lawyer.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/signin')
def signin_add():
    email_receive = request.form['email_receive']
    password_receive = request.form['password_receive']
    print(email_receive,password_receive)
    signin_add_data = {
        'email':email_receive, 
        'password':password_receive, 
    }
    db.user_info.insert_one(signin_add_data)    

    return jsonify({'result':'success'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)




