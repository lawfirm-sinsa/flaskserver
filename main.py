<<<<<<< HEAD
from flask import Flask, request, jsonify, render_template, url_for, Blueprint, redirect
from flask_pymongo import PyMongo
import bcrypt
import requests

'''from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client.dbLFD'''
=======
from flask import Flask, request, jsonify, render_template, url_for, redirect, session
import requests

from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client.dbLFD
>>>>>>> 1ba04dce14cef0089c98fefbb6efffaeefce2ff5

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'dbLFD'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/dbLFD'

mongo = PyMongo(app)

@app.route('/')
def home():
    if 'username' in session:
        return 'you are logged in as' + sesseion['username']    

    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name':request.form['username']})
    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('index'))

    return 'Invalid username/password combination'

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        return 'That username already exists!'

    return render_template('register.html')

@app.route('/lawyer')
def lawyer():
    return render_template('lawyer.html')

<<<<<<< HEAD
'''@app.route('/signin')
def signin():
    return render_template('signin.html')'''

'''@app.route('/signin')
=======
@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/signin')
>>>>>>> 1ba04dce14cef0089c98fefbb6efffaeefce2ff5
def signin_add():
    email_receive = request.form['email_receive']
    password_receive = request.form['password_receive']
    print(email_receive,password_receive)
    signin_add_data = {
        'email':email_receive, 
        'password':password_receive, 
    }
    db.user_info.insert_one(signin_add_data)    

<<<<<<< HEAD
    return jsonify({'result':'success'})'''
=======
    return jsonify({'result':'success'})
>>>>>>> 1ba04dce14cef0089c98fefbb6efffaeefce2ff5

if __name__ == "__main__":
    app.secret_key = 'mysecret'
    app.run(host="0.0.0.0", port=80, debug=True)




