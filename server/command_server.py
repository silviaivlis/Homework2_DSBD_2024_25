from proto import op_pb2, op_pb2_grpc
from services import User_Command_Service
from operations import RegisterUserCommand, UpdateTickerCommand, UpdateValuesCommand, DeleteUserCommand

class UserCommandService(op_pb2_grpc.User_command_serviceServicer):
    #------------------------------------------------------------FUNZIONE_1 
    def RegisterUser(self,request,context):
        command = RegisterUserCommand(
            email = request.email,
            ticker = request.ticker,
            requestId = request.requestId,
            highValue = request.highValue,
            lowValue = request.lowValue
        )
        result = User_Command_Service.handle_register_user(command)
        return op_pb2.RegUserResponse(message=result["message"])
        
    #------------------------------------------------------------FUNZIONE_2 
    def UpdateTicker(self,request,context):
        command = UpdateTickerCommand(
            email = request.email,
            ticker = request.ticker,
            requestId = request.requestId
        )
        result = User_Command_Service.handle_update_ticker(command)
        return op_pb2.UpdateTickerResponse(message=result["message"])

    #------------------------------------------------------------FUNZIONE_3 
    def UpdateValues(self,request,context):
        command = UpdateValuesCommand(
            email = request.email,
            requestId = request.requestId,
            highValue = request.highValue,
            lowValue = request.lowValue
        )
        result = User_Command_Service.handle_update_values(command)
        return op_pb2.UpdateValuesResponse(message=result["message"])
    
    #------------------------------------------------------------FUNZIONE_4 
    def DeleteUser(self,request,context):
        command = DeleteUserCommand(
            email = request.email,
            requestId = request.requestId
        )
        result = User_Command_Service.handle_delete_user(command)
        return op_pb2.DeleteUserResponse(message=result["message"])
