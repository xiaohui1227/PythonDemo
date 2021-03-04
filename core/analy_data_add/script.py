from proto.thing_pb2 import DataAddRes


def analy_data_add(params):
    print(params)
    return DataAddRes(analy_data=1)