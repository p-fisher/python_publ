from flask import Flask, render_template, redirect, request

from users import User

app = Flask(__name__)

# app.secret_key="Considering the many times I..."

@app.route('/users')
def users():
    return render_template('Read-All.html',users = User.get_all())

@app.route('/users/new')
def create_new():
    return render_template('Create.html')

@app.route('/users/create', methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')

@app.route('/')
def index():
    return redirect('/users')


@app.errorhandler(404)
def not_found(e): # inbuilt function which takes error as parameter
    return f"That's a no-go on the url. Sorry." # defining function

if __name__=="__main__":   # Ensure this runs directly and not from a diff module
    app.run(debug=True)    # Run the app in debug mode.