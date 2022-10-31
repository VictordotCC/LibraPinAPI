import os
from datetime import datetime
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Usuario, Board, Pin, Categoria, PinCategoria
from flask_cors import CORS, cross_origin

# 3. instanciamos la app
app = Flask(__name__)

cors = CORS(app)
#app.config['CORS_HEADERS'] = 'Content-Type'


app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

Migrate(app, db)

@cross_origin
@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('correo')
    password = request.json.get('password')

    user = Usuario.query.filter_by(correo=email, password=password).first()
    if user:
        return jsonify(data=user.serialize(), status=200), 200
    else:
        return jsonify(data="Credenciales inválidas", status=403), 403
    

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
        if (Usuario.query.filter_by(correo=correo).first() is None and 
            Usuario.query.filter_by(nombre=nombre).first() is None):
            usuario = Usuario(nombre=nombre, correo=correo, password=password)
            usuario.save()
            return jsonify(data=usuario.serialize(), status=200), 200
        return jsonify(data="El usuario/correo ya existe", status=400), 400
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
        titulo = request.json.get('titulo', None)
        contenido = request.json.get('descripcion', None)
        imagen = request.json.get('imagen', None)
        usuario = request.json.get('user_id', None)
        pin = Pin(titulo=titulo, contenido=contenido, imagen=imagen, usuario_id=usuario)
        pin.save()
        return jsonify(data=pin.serialize(), status=200), 200
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

@app.route('/pin-categoria', methods=['GET', 'POST', 'PUT', 'DELETE'])
@cross_origin()
def pin_categoria():
    if request.method == 'GET':
        pin_categoria = PinCategoria.query.all()
        return jsonify([pin_categoria.serialize() for pin_categoria in pin_categoria]), 200
    elif request.method == 'POST':
        pin_id = request.json.get('idPin', None)
        categoria_id = request.json.get('idCategoria', None)
        pin_categoria = PinCategoria(pin_id=pin_id, categoria_id=categoria_id)
        pin_categoria.save()
        return jsonify(data=pin_categoria.serialize(), status=200), 200
    elif request.method == 'PUT':
        pin_id = request.json.get('pin_id', None)
        categoria_id = request.json.get('categoria_id', None)
        pin_categoria = PinCategoria.query.get(id)
        pin_categoria.pin_id = pin_id
        pin_categoria.categoria_id = categoria_id
        pin_categoria.update()
        return jsonify(pin_categoria.serialize()), 200
    elif request.method == 'DELETE':
        pin_categoria = PinCategoria.query.get(id)
        pin_categoria.delete()
        return jsonify(pin_categoria.serialize()), 200

@app.route('/categoria/<id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@cross_origin()
def categoria(id):
    if request.method == 'GET':
        if id == 'all':
            categoria = Categoria.query.all()
            return jsonify([categoria.serialize() for categoria in categoria]), 200
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



if __name__ == '__main__':
    app.run(port=8000, debug=True)