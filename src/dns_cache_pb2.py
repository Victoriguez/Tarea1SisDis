# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dns_cache.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x64ns_cache.proto\x12\x03\x64ns\"\x1c\n\nDNSRequest\x12\x0e\n\x06\x64omain\x18\x01 \x01(\t\",\n\x0b\x44NSResponse\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x11\n\tcache_hit\x18\x02 \x01(\x08\x32;\n\x08\x44NSCache\x12/\n\nResolveDNS\x12\x0f.dns.DNSRequest\x1a\x10.dns.DNSResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dns_cache_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_DNSREQUEST']._serialized_start=24
  _globals['_DNSREQUEST']._serialized_end=52
  _globals['_DNSRESPONSE']._serialized_start=54
  _globals['_DNSRESPONSE']._serialized_end=98
  _globals['_DNSCACHE']._serialized_start=100
  _globals['_DNSCACHE']._serialized_end=159
# @@protoc_insertion_point(module_scope)
