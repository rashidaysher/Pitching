import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.urandom(79)
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:new_password@localhost/postgres'
   
   
   
    
