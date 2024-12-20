# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import op_pb2 as op__pb2

GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in op_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class User_command_serviceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterUser = channel.unary_unary(
                '/User_command_service/RegisterUser',
                request_serializer=op__pb2.RegUserRequest.SerializeToString,
                response_deserializer=op__pb2.RegUserResponse.FromString,
                _registered_method=True)
        self.UpdateTicker = channel.unary_unary(
                '/User_command_service/UpdateTicker',
                request_serializer=op__pb2.UpdateTickerRequest.SerializeToString,
                response_deserializer=op__pb2.UpdateTickerResponse.FromString,
                _registered_method=True)
        self.UpdateValues = channel.unary_unary(
                '/User_command_service/UpdateValues',
                request_serializer=op__pb2.UpdateValuesRequest.SerializeToString,
                response_deserializer=op__pb2.UpdateValuesResponse.FromString,
                _registered_method=True)
        self.DeleteUser = channel.unary_unary(
                '/User_command_service/DeleteUser',
                request_serializer=op__pb2.DeleteUserRequest.SerializeToString,
                response_deserializer=op__pb2.DeleteUserResponse.FromString,
                _registered_method=True)


class User_command_serviceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegisterUser(self, request, context):
        """Funzionalità di gestione degli utenti
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTicker(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateValues(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_User_command_serviceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterUser': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterUser,
                    request_deserializer=op__pb2.RegUserRequest.FromString,
                    response_serializer=op__pb2.RegUserResponse.SerializeToString,
            ),
            'UpdateTicker': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTicker,
                    request_deserializer=op__pb2.UpdateTickerRequest.FromString,
                    response_serializer=op__pb2.UpdateTickerResponse.SerializeToString,
            ),
            'UpdateValues': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateValues,
                    request_deserializer=op__pb2.UpdateValuesRequest.FromString,
                    response_serializer=op__pb2.UpdateValuesResponse.SerializeToString,
            ),
            'DeleteUser': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteUser,
                    request_deserializer=op__pb2.DeleteUserRequest.FromString,
                    response_serializer=op__pb2.DeleteUserResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'User_command_service', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('User_command_service', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class User_command_service(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegisterUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/User_command_service/RegisterUser',
            op__pb2.RegUserRequest.SerializeToString,
            op__pb2.RegUserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateTicker(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/User_command_service/UpdateTicker',
            op__pb2.UpdateTickerRequest.SerializeToString,
            op__pb2.UpdateTickerResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateValues(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/User_command_service/UpdateValues',
            op__pb2.UpdateValuesRequest.SerializeToString,
            op__pb2.UpdateValuesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/User_command_service/DeleteUser',
            op__pb2.DeleteUserRequest.SerializeToString,
            op__pb2.DeleteUserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class User_query_serviceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetLatestValue = channel.unary_unary(
                '/User_query_service/GetLatestValue',
                request_serializer=op__pb2.GetLatestValueRequest.SerializeToString,
                response_deserializer=op__pb2.GetLatestValueResponse.FromString,
                _registered_method=True)
        self.CalcAvarageValue = channel.unary_unary(
                '/User_query_service/CalcAvarageValue',
                request_serializer=op__pb2.CalcAvarageValueRequest.SerializeToString,
                response_deserializer=op__pb2.CalcAvarageValueResponse.FromString,
                _registered_method=True)


class User_query_serviceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetLatestValue(self, request, context):
        """Funzionalità di recupero delle informazioni
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CalcAvarageValue(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_User_query_serviceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetLatestValue': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLatestValue,
                    request_deserializer=op__pb2.GetLatestValueRequest.FromString,
                    response_serializer=op__pb2.GetLatestValueResponse.SerializeToString,
            ),
            'CalcAvarageValue': grpc.unary_unary_rpc_method_handler(
                    servicer.CalcAvarageValue,
                    request_deserializer=op__pb2.CalcAvarageValueRequest.FromString,
                    response_serializer=op__pb2.CalcAvarageValueResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'User_query_service', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('User_query_service', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class User_query_service(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetLatestValue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/User_query_service/GetLatestValue',
            op__pb2.GetLatestValueRequest.SerializeToString,
            op__pb2.GetLatestValueResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CalcAvarageValue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/User_query_service/CalcAvarageValue',
            op__pb2.CalcAvarageValueRequest.SerializeToString,
            op__pb2.CalcAvarageValueResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
