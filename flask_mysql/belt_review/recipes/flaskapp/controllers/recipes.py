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
    user_data = {
        "id": session['id']
    }
    user=User.get_by_id(user_data)                        # this breaks the page if selecting any but first recipe
    this_recipe=Recipe.get_by_id(data)
    return render_template('details.html',user=user,recipe=this_recipe)



@app.route('/add')
def new_recipe():
    # if 'id' not in session:
    #     return redirect('/logout')           # used only in GET method routes
    # data = {
    #     "id":session['user_id']                      # dont remember why i commented this out - did it break or did i decide to come back to it?
    # }
    return render_template('add_recipe.html')


@app.route('/edit_load_recipe/<int:id>')
def edit_load_recipe(id):
    data = {
        "id": id
    }
    user_data = {
        "id":session['id']                          #this has to be off bc session stuff screwed up; this means the return below must ezclude user portion or it also will fail
    }
    user=User.get_by_id(user_data)
    this_recipe=Recipe.get_by_id(data)
    return render_template("edit_recipe.html",user=user,recipe=this_recipe)
    # return render_template("edit_recipe.html",edit=Recipe.get_by_id(data))
    # return render_template("edit_recipe.html",edit=Recipe.get_by_id(data),user=User.get_by_id(user_data))



@app.route('/edit_save_recipe', methods=['POST'])
def edit_save_recipe():
    data = {
        "id": request.form['id'],
        "r_name": request.form["r_name"],
        "r_info": request.form["r_info"],
        "instructions": request.form["instructions"],
        "under30": request.form["under30"],
        "last_made": request.form["last_made"],
        # "user_id": session["id"]
    }
    Recipe.update(data)
    return redirect('/success')



@app.route('/create/recipe',methods=['POST'])
def create_recipe():
    # if 'user_id' not in session:
    #     return redirect('/logout')
    # if not Recipe.validate_recipe(request.form):            # session stuff a mess save for later
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









# having thse enabled in both controllers breaks the app

# @app.route('/exit', methods=['POST'])
# def sign_out():
#     session.clear()
#     return redirect('/')


# @app.errorhandler(404)
# def not_found(e): # inbuilt function which takes error as parameter
#     return f"That's a no-go on the url. Sorry." # defining function"""