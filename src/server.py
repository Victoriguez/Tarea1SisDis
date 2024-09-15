import csv
import random
import grpc
import redis
import subprocess
import time
from concurrent import futures
import dns_cache_pb2
import dns_cache_pb2_grpc
import os
from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Path del archivo CSV con los dominios de 3er nivel
csv_file_path = os.path.join(os.path.dirname(__file__), 'data/3rd_lev_domains.csv')

# Cargar 50 mil dominios del dataset
def cargar_dominios(csv_file, limite=50000):
    dominios = []
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i >= limite:
                break
            dominios.append(row[0])
    return dominios

# Generar 75 mil consultas (algunas repetidas)
def generar_consultas(dominios, num_consultas=75000):
    return random.choices(dominios, k=num_consultas)

# Resolver dominio con medición de tiempos
def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado, cache_hit = func(*args, **kwargs)
        fin = time.time()
        return resultado, cache_hit, fin - inicio
    return wrapper

@medir_tiempo
def resolver_dominio(domain):
    # Verificar si el dominio está en caché
    ip = cache.get(domain)
    if ip:
        return ip.decode('utf-8'), True  # Cache Hit
    else:
        # Si no está en caché, usar DIG
        result = subprocess.run(['dig', '+short', domain], stdout=subprocess.PIPE)
        ip_address = result.stdout.decode('utf-8').strip()
        if ip_address:
            cache.set(domain, ip_address)
        return ip_address, False  # Cache Miss

# Clase del servicio gRPC
class DNSCacheService(dns_cache_pb2_grpc.DNSCacheServicer):
    def ResolveDNS(self, request, context):
        domain = request.domain
        ip, cache_hit, tiempo_respuesta = resolver_dominio(domain)
        print(f"Dominio: {domain}, IP: {ip}, Cache Hit: {cache_hit}, Tiempo: {tiempo_respuesta:.6f} seg")
        return dns_cache_pb2.DNSResponse(ip=ip, cache_hit=cache_hit)

# Configurar y levantar el servidor gRPC
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dns_cache_pb2_grpc.add_DNSCacheServicer_to_server(DNSCacheService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

# Ejecutar la simulación
if __name__ == "__main__":
    # Conectar a Redis
    cache = redis.StrictRedis(host='redis-cache', port=6379)

    # Cargar 50 mil dominios
    dominios = cargar_dominios(csv_file_path)

    # Generar 75 mil consultas
    consultas = generar_consultas(dominios)

    # Diccionario para almacenar la frecuencia de las consultas
    frecuencia_consultas = defaultdict(int)

    # Simular las 75 mil consultas DNS
    for domain in consultas:
        # Aumentar la frecuencia del dominio
        frecuencia_consultas[domain] += 1
        print(f"Resolviendo {domain}...")

    # Aquí va la lógica para invocar el servidor gRPC para resolver el dominio

    # Extraer los valores de las frecuencias
    frecuencias = list(frecuencia_consultas.values())

    # Crear el histograma de la distribución de frecuencias
    plt.figure(figsize=(10, 6))
    plt.hist(frecuencias, bins=50, edgecolor='black')
    plt.title('Distribución de Frecuencias de las Consultas DNS')
    plt.xlabel('Número de veces que un dominio fue consultado')
    plt.ylabel('Frecuencia')
    plt.grid(True)

    # Mostrar el gráfico
    plt.show()

    serve()
