import grpc, time

from bin.server import testServer
from proto import thing_pb2_grpc
from concurrent import futures



def server(port=5008, works=10):
    # 启动 rpc 服务, 并发为 10
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=works))
    thing_pb2_grpc.add_testServerServicer_to_server(testServer(), server)
    server.add_insecure_port('[::]:{}'.format(port))
    server.start()
    try:
        while True:
            time.sleep(60*60*24) # one day in seconds
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    server()