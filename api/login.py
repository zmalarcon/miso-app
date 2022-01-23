from flask import Blueprint, request
from connections.db_connection import DBConnection
from injector import inject
from sqlalchemy.exc import NoResultFound
from model.usuario_model import Usuario
from model.sesion_model import Sesion, pydantic_parser
from middleware.request import schema
from stress.cpu import consumir_cpu

login_api = Blueprint('login_api', __name__)

# Proceso de login
@login_api.route('', methods=['POST'])
def autenticar(db_connection: DBConnection):
    try:
        username = request.json["username"]
        result = db_connection.db.session.query(Usuario).filter(Usuario.username == username).one()
        if not result.verify_password(request.json["password"]):
            raise NoResultFound
    except NoResultFound:
        return {"message": "Usuario o contraseña invalida"}, 404

    try:
        sesion = db_connection.db.session.query(Sesion).filter(Sesion.user_id == result.id).one()
    except NoResultFound:
        sesion = None

    db_sesion = Sesion(user_id = result.id)

    # Realizar la transacción
    if sesion != None:
        db_connection.db.session.delete(sesion)
        db_connection.db.session.flush()
    db_connection.db.session.add(db_sesion)
    db_connection.db.session.commit()
    db_connection.db.session.refresh(db_sesion)

    sesion = pydantic_parser.from_orm(db_sesion).dict()
    return sesion
