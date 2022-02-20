from flaskapp import app
from flask import render_template, redirect, request, session
from flaskapp.models.user import User
from flaskapp.models.recipe import Recipe
from flask import flash
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)



@app.route('/details/<int:num>')
def show_recipe(num):
    data = {
        # "id": session['id'] # how can i have two called id here? there's the session id and the id as num
        "id": num
    }
    user=User.get_by_id(data)
    this_recipe=Recipe.get_by_id(data)
    return render_template('details.html',user=user,recipe=this_recipe)

"""@app.route('/dojos/<int:num>')
def detail_dojo(num):
    id = {
        "id": num
    }
    this_dojo = Dojo.get_one_id(id)
    return render_template("dojo_show.html", dojo = this_dojo)"""

"""@app.route('/')
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
    # if 'f_name' not in session:
    #     return redirect('/')
    data = {
        "id": session['id']
    }
    user=User.get_by_id(data)
    recipes=Recipe.get_all()
    return render_template('success.html',user=user,recipes=recipes)


@app.route('/exit', methods=['POST'])
def sign_out():
    session.clear()
    return redirect('/')


@app.errorhandler(404)
def not_found(e): # inbuilt function which takes error as parameter
    return f"That's a no-go on the url. Sorry." # defining function"""