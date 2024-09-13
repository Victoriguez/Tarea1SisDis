import grpc
import redis
import subprocess
from concurrent import futures
import dns_cache_pb2
import dns_cache_pb2_grpc

# Conectar a Redis
cache = redis.StrictRedis(host='redis-cache', port=6379)

class DNSCacheService(dns_cache_pb2_grpc.DNSCacheServicer):
    def ResolveDNS(self, request, context):
        domain = request.domain
        # Verificar si el dominio está en caché
        cached_ip = cache.get(domain)
        if cached_ip:
            return dns_cache_pb2.DNSResponse(ip=cached_ip.decode('utf-8'), cache_hit=True)
        
        # Si no está en caché, realizar la consulta con DIG
        result = subprocess.run(['dig', '+short', domain], stdout=subprocess.PIPE)
        ip_address = result.stdout.decode('utf-8').strip()

        # Almacenar el resultado en caché
        if ip_address:
            cache.set(domain, ip_address)

        return dns_cache_pb2.DNSResponse(ip=ip_address, cache_hit=False)

# Configurar y levantar el servidor gRPC
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dns_cache_pb2_grpc.add_DNSCacheServicer_to_server(DNSCacheService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
