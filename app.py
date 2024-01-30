from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

import pymysql

db = pymysql.connect(
    host="mysqldb.cd2pfftf5k62.us-east-2.rds.amazonaws.com",
    port=3306,
    user="admin",
    password="adminadmin",
    db="mysqldb"
)

def create_user_table():
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employee (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            age INT,
            city VARCHAR(255),
            basic_salary INT,
            hra INT,
            total_salary INT
        )
    ''')
    db.commit()

create_user_table()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/users')
def users():
    cursor = db.cursor()
    cursor.execute('SELECT * FROM employee')
    users = cursor.fetchall()
    return render_template('users.html', users=users)

@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        username = request.form['username']
        age = request.form['age']
        city = request.form['city']
        total_salary = request.form['total_salary']
        hra_perc = 0.4
        total_salary = int(total_salary)

        hra = total_salary * hra_perc
        basic_salary = total_salary - hra

        cursor = db.cursor()
        cursor.execute('INSERT INTO employee (username, age, city, basic_salary, hra, total_salary) VALUES (%s, %s, %s, %s, %s, %s)',
                       (username, age, city, basic_salary, hra, total_salary))
        db.commit()

        return redirect(url_for('create_user'))

    return render_template('create_user.html')

@app.route('/delete_user/<int:id>')
def delete_user(id):
    cursor = db.cursor()
    cursor.execute('DELETE FROM employee WHERE id = %s', (id,))
    db.commit()

    cursor.execute('ALTER TABLE employee AUTO_INCREMENT = 1;')
    db.commit()

    return redirect(url_for('users'))

if __name__ == '__main__':
    app.run(debug=True)

