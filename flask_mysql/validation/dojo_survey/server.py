from config.mysqlconnection import connectToMySQL

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key="Considering the many times one may choose"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def formprocess():
    print("Got Post Info")
    # Here we add two properties to session to store the name and email
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect("/result")	 

@app.route("/result")
def formresult():
    # return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])
    return render_template('result.html')


@app.errorhandler(404)
def not_found(e): # inbuilt function which takes error as parameter
    return f"That's a no-go on the url. Sorry." # defining function


if __name__=="__main__":   # Ensure this runs directly and not from a diff module
    app.run(debug=True)    # Run the app in debug mode.