# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de configuración
COPY config /app/config

# Copia el resto de los archivos de la aplicación
COPY . /app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Establece la variable de entorno para el entorno de ejecución
# Puedes cambiar 'local' por 'prod' según el entorno
ENV ENV=local

# Expone el puerto en el que la aplicación se ejecutará
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]