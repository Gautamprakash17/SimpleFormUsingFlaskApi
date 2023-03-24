from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    collection.insert_one({'name': name, 'email': email, 'phone': phone})
    return redirect('/data')

@app.route('/data')
def data():
    data = list(collection.find())
    return render_template('data.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
