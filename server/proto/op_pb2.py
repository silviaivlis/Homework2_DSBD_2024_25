# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: op.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'op.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x08op.proto\"g\n\x0eRegUserRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x0e\n\x06ticker\x18\x02 \x01(\t\x12\x11\n\trequestId\x18\x03 \x01(\t\x12\x11\n\thighValue\x18\x04 \x01(\x01\x12\x10\n\x08lowValue\x18\x05 \x01(\x01\"\"\n\x0fRegUserResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"G\n\x13UpdateTickerRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x0e\n\x06ticker\x18\x02 \x01(\t\x12\x11\n\trequestId\x18\x03 \x01(\t\"\'\n\x14UpdateTickerResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\\\n\x13UpdateValuesRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x11\n\trequestId\x18\x02 \x01(\t\x12\x11\n\thighValue\x18\x03 \x01(\x01\x12\x10\n\x08lowValue\x18\x04 \x01(\x01\"\'\n\x14UpdateValuesResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"5\n\x11\x44\x65leteUserRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x11\n\trequestId\x18\x02 \x01(\t\"%\n\x12\x44\x65leteUserResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"&\n\x15GetLatestValueRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"Y\n\x16GetLatestValueResponse\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x0e\n\x06ticker\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x01\x12\x11\n\ttimestamp\x18\x04 \x01(\t\"7\n\x17\x43\x61lcAvarageValueRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\"O\n\x18\x43\x61lcAvarageValueResponse\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x0e\n\x06ticker\x18\x02 \x01(\t\x12\x14\n\x0c\x61verageValue\x18\x03 \x01(\x01\x32\xfa\x01\n\x14User_command_service\x12\x31\n\x0cRegisterUser\x12\x0f.RegUserRequest\x1a\x10.RegUserResponse\x12;\n\x0cUpdateTicker\x12\x14.UpdateTickerRequest\x1a\x15.UpdateTickerResponse\x12;\n\x0cUpdateValues\x12\x14.UpdateValuesRequest\x1a\x15.UpdateValuesResponse\x12\x35\n\nDeleteUser\x12\x12.DeleteUserRequest\x1a\x13.DeleteUserResponse2\xa0\x01\n\x12User_query_service\x12\x41\n\x0eGetLatestValue\x12\x16.GetLatestValueRequest\x1a\x17.GetLatestValueResponse\x12G\n\x10\x43\x61lcAvarageValue\x12\x18.CalcAvarageValueRequest\x1a\x19.CalcAvarageValueResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'op_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REGUSERREQUEST']._serialized_start=12
  _globals['_REGUSERREQUEST']._serialized_end=115
  _globals['_REGUSERRESPONSE']._serialized_start=117
  _globals['_REGUSERRESPONSE']._serialized_end=151
  _globals['_UPDATETICKERREQUEST']._serialized_start=153
  _globals['_UPDATETICKERREQUEST']._serialized_end=224
  _globals['_UPDATETICKERRESPONSE']._serialized_start=226
  _globals['_UPDATETICKERRESPONSE']._serialized_end=265
  _globals['_UPDATEVALUESREQUEST']._serialized_start=267
  _globals['_UPDATEVALUESREQUEST']._serialized_end=359
  _globals['_UPDATEVALUESRESPONSE']._serialized_start=361
  _globals['_UPDATEVALUESRESPONSE']._serialized_end=400
  _globals['_DELETEUSERREQUEST']._serialized_start=402
  _globals['_DELETEUSERREQUEST']._serialized_end=455
  _globals['_DELETEUSERRESPONSE']._serialized_start=457
  _globals['_DELETEUSERRESPONSE']._serialized_end=494
  _globals['_GETLATESTVALUEREQUEST']._serialized_start=496
  _globals['_GETLATESTVALUEREQUEST']._serialized_end=534
  _globals['_GETLATESTVALUERESPONSE']._serialized_start=536
  _globals['_GETLATESTVALUERESPONSE']._serialized_end=625
  _globals['_CALCAVARAGEVALUEREQUEST']._serialized_start=627
  _globals['_CALCAVARAGEVALUEREQUEST']._serialized_end=682
  _globals['_CALCAVARAGEVALUERESPONSE']._serialized_start=684
  _globals['_CALCAVARAGEVALUERESPONSE']._serialized_end=763
  _globals['_USER_COMMAND_SERVICE']._serialized_start=766
  _globals['_USER_COMMAND_SERVICE']._serialized_end=1016
  _globals['_USER_QUERY_SERVICE']._serialized_start=1019
  _globals['_USER_QUERY_SERVICE']._serialized_end=1179
# @@protoc_insertion_point(module_scope)