import os
import sys
import grpc
sys.path.append(os.path.abspath('./'))
from proto import thing_pb2
from proto import thing_pb2_grpc
from bin import *

_HOST = '127.0.0.1'
_PORT = '5008'


def main():
    with grpc.insecure_channel("{0}:{1}".format(_HOST, _PORT)) as channel:
        client = thing_pb2_grpc.testServerStub(channel=channel)
        params = {"base_data":1}
        response = client.analy_data_add(thing_pb2.DataAddReq(**params))
    print("received: ", response)


if __name__ == '__main__':
    server()