from flaskapp import app

#every new controller file needs to be imported here
from flaskapp.controllers import emails

# app.secret_key="Considering the many times one may look to a higher power..."

if __name__=="__main__":   # Ensure this runs directly and not from a diff module
    app.run(debug=True)    # Run the app in debug mode.