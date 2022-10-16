import os
from datetime import datetime
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Usuario, Board, Pin, Categoria, Tag
from flask_cors import CORS, cross_origin

# 3. instanciamos la app
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.url_map.strict_slashes = False

app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

Migrate(app, db)

#Definir rutas

if __name__ == '__main__':
    app.run(port=5000, debug=True)