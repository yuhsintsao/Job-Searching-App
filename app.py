from flask import Flask, render_template, request, session, flash, redirect, url_for
from views.menu import menu_blueprint
from models.auth import Auth, ErrorHandlers, required_login
from common.database import Database
from pymongo import MongoClient
import os
import pandas as pd

app = Flask(__name__) # '__main__'
app.secret_key = "0000"
app.config.update(
    DB_URI=os.environ.get('MONGODB_URI'),
    ADMIN=os.environ.get('ADMIN'),
    DB_NAME=os.environ.get('DEFAULT_DB'),
)

def insertStaticDataIntoDatabase():
    client = pymongo.MongoClient(app.config['DB_URI'])
    company = client[app.config['DB_NAME']]['company']
    job = client[app.config['DB_NAME']]['job']

    dict_job = pd.read_csv("./data/NVDA.csv").to_dict(orient='records')
    dict_company = pd.read_csv("./data/iNVDA.csv").to_dict(orient='records')

    company.insert_many(dict_company)
    job.insert_many(dict_job)
    client.close()

app.register_blueprint(menu_blueprint, url_prefix="/menu")

@app.before_first_request   
def initialize_database():
    insertStaticDataIntoDatabase()
    Database.initialize(app.config['DB_URI'], app.config['DB_NAME'])

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    app.logger.debug('Redirecting...')
    return render_template('home.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            Auth.register(username, password)
            session['username'] = username
            return redirect(url_for('menu.getstart'))
        except ErrorHandlers.ErrorHandler as e:
            flash(e.message, 'error')

    return render_template('/register.html')

@app.route('/login', methods=['GET','POST'])
def login():  
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            Auth.login(username, password)
            session['username'] = username
            return redirect(url_for('menu.getstart'))
        except ErrorHandlers.ErrorHandler as e:
            flash(e.message, 'error')

    return render_template('/login.html')

@app.route('/logout')
def logout():
    session['username'] = None
    return redirect(url_for('home'))  



if __name__ == '__main__':
    app.run(debug=True)
