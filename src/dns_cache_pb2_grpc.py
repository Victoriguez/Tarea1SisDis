# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import dns_cache_pb2 as dns__cache__pb2


class DNSCacheStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ResolveDNS = channel.unary_unary(
                '/dns.DNSCache/ResolveDNS',
                request_serializer=dns__cache__pb2.DNSRequest.SerializeToString,
                response_deserializer=dns__cache__pb2.DNSResponse.FromString,
                )


class DNSCacheServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ResolveDNS(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DNSCacheServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ResolveDNS': grpc.unary_unary_rpc_method_handler(
                    servicer.ResolveDNS,
                    request_deserializer=dns__cache__pb2.DNSRequest.FromString,
                    response_serializer=dns__cache__pb2.DNSResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dns.DNSCache', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DNSCache(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ResolveDNS(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dns.DNSCache/ResolveDNS',
            dns__cache__pb2.DNSRequest.SerializeToString,
            dns__cache__pb2.DNSResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
