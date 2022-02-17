from flaskapp import app
from flask import render_template, redirect, request
from ..models import email


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def add_email(): #or should this be def index():
    # if there are errors:
    # We call the staticmethod on email model to validate
    if not email.Email.validate_email(request.form):
        # redirect to the route where the email form is rendered.
        return redirect('/')
    # else no errors:
    email.Email.save(request.form)
    return redirect("/success")
    # return render_template('index.html')


# #this makes the user start over; assigment may just want them to correct and resubmit
# @app.route('/error')
# def on_err():
#     return redirect('index.html')


@app.route('/success')
def success():
    return render_template('success.html', emails=email.Email.get_all(), last_email=email.Email.get_all())


@app.errorhandler(404)
def not_found(e): # inbuilt function which takes error as parameter
    return f"That's a no-go on the url. Sorry." # defining function




"""
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process',methods=['POST'])
def process():
    if not Email.is_valid(request.form):
        return redirect('/')
    Email.save(request.form)
    return redirect('/results')


@app.route('/results')
def results():
    return render_template("results.html",emails=Email.get_all())

"""
