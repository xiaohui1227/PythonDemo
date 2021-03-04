from core.analy_data_add.script import analy_data_add
from proto import  thing_pb2_grpc

class testServer(thing_pb2_grpc.testServerServicer):
    def analy_data_add(self, request, context):
        response = analy_data_add(request)
        return response


