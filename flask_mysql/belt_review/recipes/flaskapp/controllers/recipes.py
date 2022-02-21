from flaskapp import app
from flask import render_template, redirect, request, session
from flaskapp.models.user import User
from flaskapp.models.recipe import Recipe
from flask import flash
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)



@app.route('/details/<int:id>')
def show_recipe(id):
    data = {
        # "id": session['id'] # how can i have two called id here? there's the session id and the id as num
        "id": id
    }
    # user=User.get_by_id(data)
    this_recipe=Recipe.get_by_id(data)
    return render_template('details.html',recipe=this_recipe)



@app.route('/add')
def new_recipe():
    # if 'user_id' not in session:
    #     return redirect('/logout')
    # data = {
    #     "id":session['user_id']
    # }
    return render_template('add_recipe.html')


@app.route('/edit/<int:id>')
def edit_recipe(id):
    data = {
        "id": id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_recipe.html",edit=Recipe.get_one(data),user=User.get_by_id(user_data))


@app.route('/create/recipe',methods=['POST'])
def create_recipe():
    # if 'user_id' not in session:
    #     return redirect('/logout')
    # if not Recipe.validate_recipe(request.form):
    #     return redirect('/new/recipe')
    data = {
        "r_name": request.form["r_name"],
        "r_info": request.form["r_info"],
        "instructions": request.form["instructions"],
        "under30": request.form["under30"],
        "last_made": request.form["last_made"],
        # "user_id": session["user_id"]
    }
    Recipe.add_recipe(data)
    return redirect('/success')


# @app.route('/exit', methods=['POST'])
# def sign_out():
#     session.clear()
#     return redirect('/')


# @app.errorhandler(404)
# def not_found(e): # inbuilt function which takes error as parameter
#     return f"That's a no-go on the url. Sorry." # defining function"""