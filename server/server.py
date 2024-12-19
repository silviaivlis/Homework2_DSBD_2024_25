from __future__ import print_function
from concurrent import futures
import grpc
from proto import op_pb2_grpc
from command_server import UserCommandService
from query_server import UserQueryService

def serve():
    port1='50051'
    port2='50052'

    commandServer = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    op_pb2_grpc.add_User_command_serviceServicer_to_server(UserCommandService(), commandServer)

    queryServer = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    op_pb2_grpc.add_User_query_serviceServicer_to_server(UserQueryService(), queryServer)

    commandServer.add_insecure_port("[::]:" + port1)
    print("CommandoServer avviato, in ascolto sulla porta: " + port1)
    commandServer.start()

    queryServer.add_insecure_port("[::]:" + port2)
    print("QueryServer avviato, in ascolto sulla porta: " + port2)
    queryServer.start()

    commandServer.wait_for_termination()
    queryServer.wait_for_termination()


if __name__ == "__main__":
    serve()