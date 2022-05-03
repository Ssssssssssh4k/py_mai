import flask
from flask import Flask, request, make_response, redirect, abort

app = Flask(__name__)
#print(name)

names = ['user1','user2', 'user3']

@app.route('/')
def index():
    return '<h1>Hello</h1>', 400

@app.route('/error')
def error():
    abort(404)

@app.route('/home')
def home():
    return redirect('/')

@app.route('/user/<name>')
def user(name):
    if name in names:
        #print name in browser
        user_agent = request.headers.get('User-Agent')
        response = make_response('<h1>Hello, %s</h1><br>Your browser is %s' % (name, user_agent))
        response.set_cookie('answer','42')
        return response
    else:
        return error()

if __name__=='__main__':
    app.run(debug=True)