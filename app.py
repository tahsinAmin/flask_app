import flask
from markupsafe import escape
from flask import Flask, abort

app = Flask(__name__) # create the flask class object

@app.route('/') #decorator defines the 
def hello():
    test = "Flask"
    return f'<h1>Hello, this is our first {flask} website!!</h1>'

@app.route('/about')
def about():
    return '<h1>"About!"</h1>'

@app.route('/capitalize/<word>/')
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))

@app.route('/add/<int:n1>/<int:n2>/')
def add(n1, n2):
    return '<h1>{}</h1>'.format(n1 + n2)


@app.route('/users/<int:user_id>/')
def greet_user(user_id):
    users = ['Bob', 'Jane', 'Adam']
    try:
        return '<h2>Hi {}</h2>'.format(users[user_id])
    except IndexError:
        abort(404)




if __name__ == '__main__':
    app.run(debug=True)