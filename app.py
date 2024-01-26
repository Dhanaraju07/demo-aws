from flask import Flask, render_template, request

app = Flask(__name__)

import rds_db as db

import pymysql

conn = pymysql.connect(
    host="mysqldb.cd2pfftf5k62.us-east-2.rds.amazonaws.com",
    port=3306,
    user="admin",
    password="adminadmin",
    db="mysqldb"
)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/users')
def get_users_data():
    details = db.get_details()
    return render_template('users.html', users=details)

@app.route('/create_user', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['username']
        age = request.form['age']
        city = request.form['city']
        db.insert_details(name, age, city)
        details = db.get_details()
        return render_template('create_user.html', var=details[-1])
    else:
        return render_template('create_user.html')

if __name__ == "__main__":
    app.run(debug=True)
