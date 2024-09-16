# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Instalar el paquete dnsutils para usar el comando 'dig'
RUN apt-get update && apt-get install -y dnsutils

# Copia los archivos de la aplicación al contenedor
COPY . .

# Instala las dependencias necesarias
RUN pip install -r requirements.txt

# Expone el puerto del servidor gRPC
EXPOSE 50051

# Comando para ejecutar el servidor gRPC
CMD ["python", "server.py"]
