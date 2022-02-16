from email_validation_exc.config.mysqlconnection import connectToMySQL
import re	# the regex module


class Emails:
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    # create a regular expression object that we'll use later   
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
    @staticmethod
    def validate_email(email):
        is_valid = True # we assume this is true
        if not EMAIL_REGEX.match(Emails['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid
    
    @classmethod
    def get_all(cls):
        query= "SELECT * FROM emails;"
        results = connectToMySQL(cls.db).query_db(query)
        emails = []
        for row in results:
            emails.append( cls(row) )
        return emails

    @classmethod
    def save(cls,data):
        query = "INSERT INTO emails (email, created_at) VALUES (%(email)s, NOW());"
        return connectToMySQL(cls.db).query_db(query,data)




"""# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User:
    @staticmethod
    def validate_user( user ):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid"""