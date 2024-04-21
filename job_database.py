#!/usr/bin/python3
import MySQLdb

def create_database(host, user, password, database_name):
    db = MySQLdb.connect(host=host, user=user, passwd=password)
    cursor = db.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS {}'.format(database_name))
    cursor.execute('USE {}'.format(database_name))
    cursor.execute('CREATE TABLE IF NOT EXISTS jobs (id INT PRIMARY KEY AUTO_INCREMENT, title VARCHAR(100), description TEXT, salary TEXT)')
    db.close()

# create_database('localhost', 'root', 'user_password', 'db_name')

def check_database(host, user, password, database_name):
    db = MySQLdb.connect(host=host, user=user, passwd=password, db=database_name)
    cursor = db.cursor()
    cursor.execute('SHOW TABLES')
    tables = cursor.fetchall()
    if len(tables) == 0:
        print('No tables found')
    else:
        print('Tables found')
    db.close()

# check_database(host='localhost', user='root', password='password', database_name='db_name')

def insert_into_database(host, user, password, database_name, job_title, job_description, salary):
    db = MySQLdb.connect(host=host, user=user, passwd=password, db=database_name)
    cursor = db.cursor()
    cursor.execute('INSERT INTO jobs (title, description, salary) VALUES (%s, %s, %s)', (job_title, job_description, salary))
    db.commit()
    db.close()


def print_database(host, user, password, database_name):
    db = MySQLdb.connect(host=host, user=user, passwd=password, db=database_name)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM jobs')
    jobs = cursor.fetchall()
    for job in jobs:
        print(job)
    db.close()

