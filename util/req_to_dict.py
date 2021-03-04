import json

from core.analy_data_add import script
from proto import thing_pb2,thing_pb2_grpc
from google.protobuf.json_format import MessageToDict

class MongoJob(thing_pb2_grpc.testServerServicer):
    def analy_data_add(self, request, context):
        request = dict(MessageToDict(request, False, True))
        try:
            response = script.analy_data_add(**request)
            return thing_pb2.DataAddRes(**response)
        except Exception as e:
            raise e