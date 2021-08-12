from fetchData import fetchData
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/data', methods=['POST'])
def my_form_post():
    text = request.form['text']
    title,image,price = fetchData(text)
    return render_template('data.html',title = title,image=image,price=price)

@app.route('/productsPage')
def productsPage():
    return render_template('productsPage.html')

if __name__ == '__main__':
    app.run(host="localhost", port=7031, debug=True)