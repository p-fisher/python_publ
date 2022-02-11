from flask import Flask, render_template
app = Flask(__name__)

# import the class from friend.py
from friend import Friend

# app.secret_key="Considering the many times one may look to a higher power..."

@app.route('/')
def index():
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", all_friends = friends)




@app.errorhandler(404)
def not_found(e): # inbuilt function which takes error as parameter
    return f"That's a no-go on the url. Sorry." # defining function

if __name__=="__main__":   # Ensure this runs directly and not from a diff module
    app.run(debug=True)    # Run the app in debug mode.
