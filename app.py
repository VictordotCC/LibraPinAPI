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

# Obtener/Crear/Actualizar/Eliminar usuarios


#Buscar por ID o Nombre?
@app.route('/usuario/<id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@cross_origin()
def usuario(id):
    if request.method == 'GET':
        usuario = Usuario.query.get(id)
        return jsonify(usuario.serialize()), 200
    elif request.method == 'POST':
        nombre = request.json.get('nombre', None)
        correo = request.json.get('correo', None)
        password = request.json.get('password', None)
        usuario = Usuario(nombre=nombre, correo=correo, password=password)
        usuario.save()
        return jsonify(usuario.serialize()), 200
    elif request.method == 'PUT':
        nombre = request.json.get('nombre', None)
        correo = request.json.get('correo', None)
        password = request.json.get('password', None)
        usuario = Usuario.query.get(id)
        usuario.nombre = nombre
        usuario.correo = correo
        usuario.password = password
        usuario.update()
        return jsonify(usuario.serialize()), 200
    elif request.method == 'DELETE':
        usuario = Usuario.query.get(id)
        usuario.delete()
        return jsonify(usuario.serialize()), 200

# Obtener/Crear/Actualizar/Eliminar boards

@app.route('/board/<id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@cross_origin()
def board(id):
    if request.method == 'GET':
        board = Board.query.get(id)
        return jsonify(board.serialize()), 200
    elif request.method == 'POST':
        nombre = request.json.get('nombre', None)
        board = Board(nombre=nombre)
        board.save()
        return jsonify(board.serialize()), 200
    elif request.method == 'PUT':
        nombre = request.json.get('nombre', None)
        board = Board.query.get(id)
        board.nombre = nombre
        board.update()
        return jsonify(board.serialize()), 200
    elif request.method == 'DELETE':
        board = Board.query.get(id)
        board.delete()
        return jsonify(board.serialize()), 200

# Obtener/Crear/Actualizar/Eliminar pins

@app.route('/pin/<id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@cross_origin()
def pin(id):
    if request.method == 'GET':
        pin = Pin.query.get(id)
        return jsonify(pin.serialize()), 200
    elif request.method == 'POST':
        nombre = request.json.get('nombre', None)
        descripcion = request.json.get('descripcion', None)
        imagen = request.json.get('imagen', None)
        pin = Pin(nombre=nombre, descripcion=descripcion, imagen=imagen)
        pin.save()
        return jsonify(pin.serialize()), 200
    elif request.method == 'PUT':
        nombre = request.json.get('nombre', None)
        descripcion = request.json.get('descripcion', None)
        imagen = request.json.get('imagen', None)
        pin = Pin.query.get(id)
        pin.nombre = nombre
        pin.descripcion = descripcion
        pin.imagen = imagen
        pin.update()
        return jsonify(pin.serialize()), 200
    elif request.method == 'DELETE':
        pin = Pin.query.get(id)
        pin.delete()
        return jsonify(pin.serialize()), 200

# Obtener/Crear/Actualizar/Eliminar categorias

@app.route('/categoria/<id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@cross_origin()
def categoria(id):
    if request.method == 'GET':
        categoria = Categoria.query.get(id)
        return jsonify(categoria.serialize()), 200
    elif request.method == 'POST':
        nombre = request.json.get('nombre', None)
        categoria = Categoria(nombre=nombre)
        categoria.save()
        return jsonify(categoria.serialize()), 200
    elif request.method == 'PUT':
        nombre = request.json.get('nombre', None)
        categoria = Categoria.query.get(id)
        categoria.nombre = nombre
        categoria.update()
        return jsonify(categoria.serialize()), 200
    elif request.method == 'DELETE':
        categoria = Categoria.query.get(id)
        categoria.delete()
        return jsonify(categoria.serialize()), 200

# Obtener/Crear/Actualizar/Eliminar tags

@app.route('/tag/<id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@cross_origin()
def tag(id):
    if request.method == 'GET':
        tag = Tag.query.get(id)
        return jsonify(tag.serialize()), 200
    elif request.method == 'POST':
        nombre = request.json.get('nombre', None)
        tag = Tag(nombre=nombre)
        tag.save()
        return jsonify(tag.serialize()), 200
    elif request.method == 'PUT':
        nombre = request.json.get('nombre', None)
        tag = Tag.query.get(id)
        tag.nombre = nombre
        tag.update()
        return jsonify(tag.serialize()), 200
    elif request.method == 'DELETE':
        tag = Tag.query.get(id)
        tag.delete()
        return jsonify(tag.serialize()), 200



if __name__ == '__main__':
    app.run(port=5000, debug=True)