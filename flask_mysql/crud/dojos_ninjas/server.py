from flask import Flask, render_template, redirect, request

# import the classes from Dojo and Ninja
from dojo import Dojo
from ninja import Ninja

app = Flask(__name__)

# app.secret_key="Could this be anymore fun?"


@app.route('/dojos')
def show_dojos():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template('dojos.html', all_dojos = dojos)


@app.route('/dojos/<int:num>')
def detail_dojo(num):
    id = {
        "id": num
    }
    this_dojo = Dojo.get_one_id(id)
    return render_template("dojo_show.html", dojo = this_dojo)


@app.route('/ninjas')
def show_ninjas():
    ninjas = Ninja.get_all()
    dojos = Dojo.get_all()
    print(ninjas)
    return render_template('ninjas.html', all_ninjas = ninjas, all_dojos = dojos)


@app.route('/new_dojo', methods=['POST'])
def new_dojo():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "name": request.form["name"],
    }
    # We pass the data dictionary into the save method from the Friend class.
    Dojo.create(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/dojos')


@app.route('/new_ninja', methods=['POST'])
def new_ninja():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "dojo_id": request.form["dojo_id"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
    }
    # We pass the data dictionary into the save method from the Friend class.
    Ninja.create(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/ninjas')


@app.errorhandler(404)
def not_found(e): # inbuilt function which takes error as parameter
    return f"That's a no-go on the url. Sorry." # defining function

if __name__=="__main__":   # Ensure this runs directly and not from a diff module
    app.run(debug=True)    # Run the app in debug mode.