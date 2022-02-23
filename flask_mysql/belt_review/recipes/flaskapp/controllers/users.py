from flaskapp import app
from flask import render_template, redirect, request, session
from flaskapp.models.user import User
from flaskapp.models.recipe import Recipe
from flask import flash
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    if not User.validate_register(request.form):
        return redirect('/')
    data = {
        "f_name": request.form['f_name'],
        "l_name": request.form['l_name'],
        "email": request.form['email'],
        # "pwd": request.form['pwd']
        "pwd": bcrypt.generate_password_hash(request.form['pwd'])
    }
    id = User.register(data)
    # session['f_name'] = request.form['f_name']
    session['id'] = id
    return redirect('/success')



@app.route('/sign_in', methods=['POST'])
def sign_in():
    user = User.sign_in(request.form)
    if not user:
        flash("Invalid Email","sign_in")
        return redirect('/')
    if not bcrypt.check_password_hash(user.pwd, request.form['pwd']):
        flash("Invalid Password","sign_in")
        return redirect('/')
    # session['f_name'] = request.form['f_name']
    session['id'] = user.id
    return redirect('/success')


@app.route('/success')
def made_it():
    if 'id' not in session:
        return redirect('/exit')           # used only in GET method routes
    data = {
        "id": session['id']
    }
    user=User.get_by_id(data)
    recipes=Recipe.get_all()
    return render_template('success.html',user=user,recipes=recipes)


@app.route('/exit')
def sign_out():
    session.clear()
    return redirect('/')


@app.errorhandler(404)
def not_found(e): # inbuilt function which takes error as parameter
    return f"That's a no-go on the url. Sorry." # defining function