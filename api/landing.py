from flask import Blueprint, request
from connections.db_connection import DBConnection
from injector import inject
from sqlalchemy.exc import NoResultFound
from model.producto_model import Producto, producto_convertir_arreglo
from middleware.request import schema
import random

from stress.cpu import consumir_cpu, consumir_ram

landing_api = Blueprint('landing_api', __name__)

# Consulta de productos para el landing page
@landing_api.route('/', methods=['GET'])
@inject
def obtener_landing(db_connection: DBConnection):
    random1 = consumir_cpu(5)
    random2 = consumir_ram(1024, 20)
    ranking = random.random()
    try:
        result = db_connection.db.session.query(Producto).filter(Producto.ranking.op('>=')(ranking)).order_by(Producto.ranking).limit(50).all()
    except NoResultFound:
        return {"message": "La orden de entrega no existe"}, 404
    result = producto_convertir_arreglo(result)
    return { "data": result, "random": str(random1)+"-"+str(random2) }
