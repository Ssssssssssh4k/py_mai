import flask
from flask import Flask, make_response, redirect, abort

app = Flask(__name__, template_folder="typical_pages")

app = Flask(__name__)
data = [{'id': 1, 'name': 'Postavte', 'surname': 'Pojaluista', 'age': 5},
        {'id': 2, 'name': 'Vladimir', 'surname': 'Putin', 'age': 69}]

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def userdata():
    retuser = ""
    for i in data:
        id = i['id']
        name = i['name']
        surname = i['surname']
        age = i['age']
        retuser += f'<h1><a href="/user/{id}"> {id}. {name} {surname} {age} </a></h1><hr style="border: 5px solid blue;">'
    return retuser

@app.route('/home')
def home():
    return redirect('/')

@app.route('/user/<id>')
def user(id):
    for i in data:
        item_id = str(i['id'])
        if item_id == id:
            response = make_response(f'<h1>Hello! </br> </br> Your name is {i["name"]} </br> Your age is {i["age"]}</h1>')
            return response
    return abort(404)

if __name__=='__main__':
    app.run(debug=True)