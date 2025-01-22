# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Instala las dependencias del sistema necesarias para compilar psycopg2
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    libpq-dev  # Esta es la librería que proporciona pg_config

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt /app/requirements.txt

# Copia la carpeta config desde app/config al contenedor
COPY app/config /app/config

# Copia el resto de los archivos de la aplicación
COPY . /app

# Actualiza pip
RUN pip install --upgrade pip

# Instala las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Establece la variable de entorno para el entorno de ejecución
ENV ENV=local

# Expone el puerto en el que la aplicación se ejecutará
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
