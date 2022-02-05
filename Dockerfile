# Imagen base
FROM python:3.9.7-slim-buster

# Copiar los archivos al contenedor
COPY . .

# Instalar dependencias
RUN pip install -r requirements.txt

# Ejecutar el gunicorn para servir la aplicacion
CMD [ "gunicorn", "-c", "gunicorn.conf.py" ]