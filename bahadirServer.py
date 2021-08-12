from fetchData import fetchData
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/data', methods=['POST'])
def my_form_post():
    text = request.form['text']
    title,image,price = deneme(text)
    return render_template('data.html',title = title,image=image,price=price)