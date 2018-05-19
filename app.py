
from flask import Flask, render_template, jsonify
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/country/<name>')
def country(name):
    cocap_list = []
    conn = sql.Connection('database.db')
    cur = conn.cursor()
    cur.execute("SELECT capital from cocap WHERE country='{}';".format(name.lower()))
    c = cur.fetchone()
    cocap_list.append(name.title())
    if not c:
        return render_template('bunked.html')
    else:
        cocap_list.append(c[0].title())
        return render_template('home.html', name=cocap_list)

@app.route('/get/<name>')
def get(name):
    cocap_list = []
    conn = sql.Connection('database.db')
    cur = conn.cursor()
    cur.execute("SELECT capital from cocap WHERE country='{}';".format(name.lower()))
    c = cur.fetchone()
    cocap_list.append(name.title())
    if not c:
        return jsonify(country = name, capital = 'Invalid country name')
    else:
        cocap_list.append(c[0].title())
        return jsonify(country = name, capital=cocap_list[1])

if __name__ == "__main__":
    app.debug = True
    app.run()
