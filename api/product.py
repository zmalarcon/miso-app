from flask import Blueprint, request
from connections.db_connection import DBConnection
from injector import inject
from sqlalchemy.exc import NoResultFound
from model.producto_model import Producto, pydantic_parser
from middleware.request import schema
from stress.cpu import consumir_cpu, consumir_ram

producto_api = Blueprint('producto_api', __name__)

# Consulta de productos
@producto_api.route('/<producto_id>', methods=['GET'])
@inject
def dar_producto(producto_id: int, db_connection: DBConnection):
    random1 = consumir_cpu(10)
    random2 = consumir_ram(1024, 20)
    try:
        result = db_connection.db.session.query(Producto).filter(Producto.id == producto_id).one()
    except NoResultFound:
        return {"message": "El producto no existe"}, 404
    producto = pydantic_parser.from_orm(result).dict()
    producto["random"] = str(random1)+"-"+str(random2)
    return producto
