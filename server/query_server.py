from proto import op_pb2, op_pb2_grpc
from services import User_Query_Service
from operations import GetLatestValueQuery, CalcAverageValueQuery

class UserQueryService(op_pb2_grpc.User_query_serviceServicer):
    #------------------------------------------------------------FUNZIONE_5 
    def GetLatestValue(self,request,context):
        query = GetLatestValueQuery(email = request.email)
        result = User_Query_Service.get_latest_value(query)
        return op_pb2.GetLatestValueResponse(
            email=result["email"],
            ticker=result["ticker"],
            value=result["value"],
            timestamp=result["timestamp"]
        )

    #------------------------------------------------------------FUNZIONE_6 
    def CalcAvarageValue(self,request,context):
        query = CalcAverageValueQuery(email = request.email, count = request.count)
        result = User_Query_Service.get_avarage_value(query)
        return op_pb2.CalcAvarageValueResponse(
            email=result["email"],
            ticker=result["ticker"],
            averageValue=result["averageValue"]
        )
