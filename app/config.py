DB_USER = 'root'
DB_PASSWORD = 'root'
DB_HOST = 'localhost'
DB_DB = 'test'

DEBUG = True
PORT = 3333
HOST = "0.0.0.0"

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'mysql://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DB_DB