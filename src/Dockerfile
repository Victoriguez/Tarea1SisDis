# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos de la aplicación al contenedor
COPY . .

# Instala las dependencias necesarias
RUN pip install -r requirements.txt

# Compilar los archivos .proto
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. dns_cache.proto

# Expone el puerto del servidor gRPC
EXPOSE 50051

# Comando para ejecutar el servidor gRPC
CMD ["python", "server.py"]
