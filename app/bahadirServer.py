from fetchData import fetchData
from flask import Flask, request, render_template, redirect
import mysql.connector

app = Flask(__name__)

config = {
        'user': 'root',
        'password': 'test',
        'host': 'db',
        'port': '3306',
    }
mydb = mysql.connector.connect(**config)

cursor = mydb.cursor()
cursor.execute("DROP DATABASE IF EXISTS products")

sql_init_query = """CREATE TABLE IF NOT EXISTS products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), image_url VARCHAR(255), price VARCHAR(255))"""

cursor.execute("CREATE DATABASE IF NOT EXISTS MyDb")
cursor.execute("USE MyDb")
cursor.execute(sql_init_query)

@app.route('/')
def init():
  return redirect('/create')

@app.route('/create')
def create():
    return render_template('Create.html')

@app.route('/createpost', methods=['POST'])
def create_post():
    text = request.form['text']
    title,image,price = fetchData(text)
    cursor = mydb.cursor()
    sql_create_query = """INSERT INTO products (name, image_url, price) VALUES (%s,%s,%s)"""
    val = (title,image,price)
    cursor.execute(sql_create_query,val)
    mydb.commit()
    return redirect('/index')

@app.route('/index')
def index():
    cursor = mydb.cursor()
    sql_index_query = """SELECT * FROM products"""
    cursor.execute(sql_index_query)
    records = cursor.fetchall()

    return render_template('Index.html', products = records)

@app.route('/details', methods=['POST'])
def details():
    product_id = request.form['id']
    cursor = mydb.cursor()
    sql_details_query = """SELECT * FROM products WHERE id = %s"""
    cursor.execute(sql_details_query,(product_id,))
    product = cursor.fetchone()
    print(product)
    if(product is None):
        return render_template('NotFound.html')
    
    return render_template('Details.html',title = product[1],image = product[2], price = product[3])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)