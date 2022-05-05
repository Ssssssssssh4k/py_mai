import flask
from flask import Flask, make_response, redirect, abort, render_template, request

app = Flask(__name__, template_folder="typical_pages")

app = Flask(__name__)
data = [{'id': 1, 'name': 'Postavte', 'surname': 'Pojaluista', 'age': 5},
        {'id': 2, 'name': 'Vladimir', 'surname': 'Putin', 'age': 69}]

@app.route('/')
def index():
    return redirect('/users')

@app.route('/home')
def home():
    return redirect('/users')

@app.route('/users')
def user_list():
    return render_template('userlist.html', data=data)

@app.route('/user/<id>')
def user_profile(id):
    for i in data:
        item_id = str(i['id'])
        if item_id == id:
            return render_template('userprofile.html', user=i)
    return abort(404)

@app.route('/registration', methods=["get", "post"])
def new_user():
    if request.method == "GET":
        return render_template("registration.html")

    name = request.form.get("name")
    surname = request.form.get("surname")
    age = request.form.get("age")

    last_id = 0
    if len(data) > 0:
        last_id = data[-1]["id"]
    data.append({"id": last_id + 1, "name": name, "surname": surname, "age": age})
    return ('<h1>Success!</h1>')
    return redirect('/users')

@app.route('/ban')
def ban():
    return render_template('jaloba.html')

if __name__=='__main__':
    app.run(debug=True)