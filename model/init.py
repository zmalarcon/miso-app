from sqlalchemy.exc import IntegrityError
from model.usuario_model import Usuario
from model.producto_model import Producto
from model.sesion_model import Sesion
import bcrypt

def instantiate_db(db) -> None:
    """
    Permite instanciar la base de datos
    Dado a que con gunicorn instanciamos varios workers,
    estos al iniciar intentaran volver a crear la base de datos.
    Lo anterior causara un error que vamos a suprimir

    :param db: Conexion a la base de datos
    """
    try:
        db.create_all()
        salt = bcrypt.gensalt(12)
        usuario1 = Usuario(email = "1@1.1", phone = "1", username = "1", salt = salt.decode("utf-8"), password = bcrypt.hashpw("1".encode('utf8'), salt).decode("utf-8"))
        db.session.add(usuario1)
        db.session.add(Usuario(email = "2@2.2", phone = "2", username = "2", salt = salt.decode("utf-8"), password = bcrypt.hashpw("2".encode('utf8'), salt).decode("utf-8")))
        #db.session.add(Usuario(email = "2@2.2", password = bcrypt.hashpw(str.encode("2222"), bcrypt.gensalt(12))))
        db.session.add(Producto(nombre = "Producto de prueba 0", descripcion = "Un producto de prueba para verificar la funcionalidad", imagen="123.png", ranking=0.1))
        db.session.add(Producto(nombre = "Producto de prueba 1", descripcion = "Un producto de prueba para verificar la funcionalidad", imagen="123.png", ranking=0.5))
        db.session.add(Producto(nombre = "Producto de prueba 2", descripcion = "Un producto de prueba para verificar la funcionalidad", imagen="123.png", ranking=1.0))
        db.session.add(Sesion(user_id = usuario1.id))
        db.session.commit()

    except IntegrityError as e:
        pass
