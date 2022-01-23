from flask import Blueprint, request
from connections.db_connection import DBConnection
from injector import inject
from sqlalchemy.exc import NoResultFound
from model.sesion_model import Sesion, pydantic_parser
from middleware.request import schema
from stress.cpu import consumir_ram

sesion_api = Blueprint('sesion_api', __name__)

# Consulta de sesiones
@sesion_api.route('/<session_id>', methods=['GET'])
@inject
def dar_sesion(session_id: int, db_connection: DBConnection):
    random2 = consumir_ram(1024*4, 30)
    try:
        result = db_connection.db.session.query(Sesion).filter(Sesion.id == session_id).one()
    except NoResultFound:
        return {"message": "La sesión no existe"}, 404
    sesion = pydantic_parser.from_orm(result).dict()
    sesion["random"] = str(random2)
    return sesion
