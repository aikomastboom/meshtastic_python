# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: environmental_measurement.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x65nvironmental_measurement.proto\"\xa1\x01\n\x18\x45nvironmentalMeasurement\x12\x13\n\x0btemperature\x18\x01 \x01(\x02\x12\x19\n\x11relative_humidity\x18\x02 \x01(\x02\x12\x1b\n\x13\x62\x61rometric_pressure\x18\x03 \x01(\x02\x12\x16\n\x0egas_resistance\x18\x04 \x01(\x02\x12\x0f\n\x07voltage\x18\x05 \x01(\x02\x12\x0f\n\x07\x63urrent\x18\x06 \x01(\x02\x42#Z!github.com/meshtastic/gomeshprotob\x06proto3')



_ENVIRONMENTALMEASUREMENT = DESCRIPTOR.message_types_by_name['EnvironmentalMeasurement']
EnvironmentalMeasurement = _reflection.GeneratedProtocolMessageType('EnvironmentalMeasurement', (_message.Message,), {
  'DESCRIPTOR' : _ENVIRONMENTALMEASUREMENT,
  '__module__' : 'environmental_measurement_pb2'
  # @@protoc_insertion_point(class_scope:EnvironmentalMeasurement)
  })
_sym_db.RegisterMessage(EnvironmentalMeasurement)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z!github.com/meshtastic/gomeshproto'
  _ENVIRONMENTALMEASUREMENT._serialized_start=36
  _ENVIRONMENTALMEASUREMENT._serialized_end=197
# @@protoc_insertion_point(module_scope)
