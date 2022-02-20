from flaskapp.config.mysqlconnection import connectToMySQL
import re	# the regex module
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
from flask import flash

class Email:
    db = "email_validn_schema"
    
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    # create a regular expression object that we'll use later   
    @staticmethod
    def validate_email(email):
        is_valid = True # we assume this is true
        if not EMAIL_REGEX.match(email['email']): 
            flash("")
            is_valid = False
        return is_valid
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL(cls.db).query_db(query)
        emails = []
        for row in results:
            emails.append( cls(row) )
        return emails

    @classmethod
    def save(cls,data):
        query = "INSERT INTO emails (email, created_at) VALUES (%(email)s, NOW());"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def get_last(cls):
        query = "SELECT * FROM emails WHERE id = (SELECT MAX(id) FROM emails);"
        last_email = connectToMySQL(cls.db).query_db(query)
        this_email = cls(last_email[0])
        return this_email
        # return cls(last_email[0])



    # @classmethod
    # def get_last(cls):
    #     query = "SELECT * FROM emails WHERE id = (SELECT MAX(id) FROM emails);"
    #     results = connectToMySQL(cls.db).query_db(query)
    #     last_email = []
    #     for row in results:
    #         last_email.append( cls(row) )
    #     return last_email




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