from flask import Flask
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
DATABASE = "privatedb"
app.secret_key = 'kekekekeke'
