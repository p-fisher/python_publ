from flaskapp.config.mysqlconnection import connectToMySQL
import re	# the regex module
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PWD_REGEX = re.compile(r'^[?=.A-Z0-9][?=.0-9A-Z].{6,}$')

from flask import flash

class Recipe:
    db = "recipes_users_schema"

    def __init__(self,data):
        self.id = data['id']
        self.r_name = data['r_name']
        self.description = data['description']
        self.r_info = data['r_info']
        self.under30 = data['under30']
        self.last_made = data['last_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def add(cls,data):
        query = "INSERT INTO users (r_name,description,r_info,under30,last_made,created_at) VALUES (%(r_name)s, %(description)s, %(r_info)s, %(under30)s, %(last_made)s, NOW());"
        print(data)
        return connectToMySQL(cls.db).query_db(query,data)
        #return from db you get is just the id


    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])









