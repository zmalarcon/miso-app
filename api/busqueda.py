from flask import Blueprint, request
from connections.db_connection import DBConnection
from injector import inject
from sqlalchemy.exc import NoResultFound
from model.producto_model import Producto, producto_convertir_arreglo
from model.palabra_model import Palabra, palabra_parser
from middleware.request import schema
from sqlalchemy.sql import func
import random

from stress.cpu import consumir_cpu, consumir_ram


busqueda_api = Blueprint('busqueda_api', __name__)

# Consulta de productos por palabras clave
@busqueda_api.route('', methods=['POST'])
@inject
def buscar_productos(db_connection: DBConnection):
    driver = db_connection.db.engine.driver
    random1 = consumir_cpu(20)
    random2 = consumir_ram(10240, 10)
    try:
        if driver == "pysqlite":
            result = db_connection.db.engine.execute("SELECT * FROM producto LIMIT 10")
        else:
            numeroPalabras = darNumeroPalabras()
            palabras = []
            for p in range(numeroPalabras):
                ranking = random.random()
                palabra = db_connection.db.session.query(Palabra).filter(Palabra.ranking.op('>=')(ranking)).order_by(Palabra.ranking).limit(1).all()[0].palabra
                palabras.append(palabra)
            filtro = " & ".join(palabras)
            result = db_connection.db.session.query(Producto).filter(
                func.to_tsvector('english', Producto.descripcion).op('@@')(func.to_tsquery('english', filtro))
            ).all()
    except NoResultFound:
        return {"message": "La busqueda no produjo resultados"}, 404
    result = producto_convertir_arreglo(result)
    return { "data": result, "random": str(random1)+"-"+str(random2) }

def darNumeroPalabras():
    numero = random.randint(0, 9)
    if numero < 5:
        return 1
    if numero < 8:
        return 2
    return 3