# Semana-1-Proyecto-Esqueleto

Repositorio con el código base del monolito utilizado para la entrega 1 del proyecto.

## Requisitos

Python 3.9

## Inicio de la aplicación

Para ejecutar el proyecto utilice los siguientes comandos:

pip install -r ./requirements.txt

Una vez instaladas las dependencias, ejecute la aplicación usando:

python app.py

### Ambiente local

Localmente la aplicación utiliza una base de datos SQlite ubicada en el archivo development.db.

### Ambiente productivo

Al inicio de la aplicación se ejecutan los siguiente comandos para cargar la configuración del ambiente:

app.config.from_envvar('APPLICATION_SETTINGS', True)
app.config.from_envvar('APPLICATION_SECRETS', True)

Se espera que las variables de entorno APPLICATION_SETTINGS y APPLICATION_SECRETS contengan rutas de acceso a archivo cfg. Para mas información ver https://flask.palletsprojects.com/en/2.0.x/config/#configuring-from-python-files

Puede colocar la variable de entorno 

APPLICATION_SECRETS=./config/example-config.cfg

para cargar la configuración de ejemplo example-config.cfg. En este ejemplo se define una cadena de conexión distinta para que la aplicación utilice otra base de datos.

Para ver un ejemplo de cómo utilizar secretos para almacenar la conexión a la base de datos, estudie los tutoriales de la semana.
