from flask import Flask, render_template,request, redirect
app = Flask(__name__)

# import the class from friend.py
from friend import Friend

# app.secret_key="Considering the many times one may look to a higher power..."

@app.route('/')
def index():
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", all_friends = friends)

from friend import Friend
@app.route('/create_friend', methods=["POST"])
def create_friend():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "occupation" : request.form["occupation"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    Friend.create(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')



@app.errorhandler(404)
def not_found(e): # inbuilt function which takes error as parameter
    return f"That's a no-go on the url. Sorry." # defining function

if __name__=="__main__":   # Ensure this runs directly and not from a diff module
    app.run(debug=True)    # Run the app in debug mode.
