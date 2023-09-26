from REST_like_socket import Server, ServerRequestHandler
from REST_like_socket import SocketClient


class SyncedResources:
    def __init__(
        self,
        isResource_host: bool,
        synchronize_to: str = None,
        host: str = "0.0.0.0",
        port: int = 59999,
    ) -> None:
        self.isResource_host = isResource_host
        self.LocalResources = dict()
        LocalResources = self.LocalResources
        self.host = host
        self.port = port
        self.link_host = synchronize_to
        self.connection = SocketClient(host=self.link_host, port=self.port)

        class CustomHandler(ServerRequestHandler):
            def set_LocalResource(self):
                self.LocalResources: dict = LocalResources

            # def custom_HandleEvent(
            #     self, bytes_data: bytes, decoded_data: str, json_data: dict
            # ):
            #     print(json_data)

            # def if_Get(self, requested_data):
            #     if requested_data == "LocalResources":
            #         self.send_response(self.LocalResources)

        if self.isResource_host:
            self.server = Server(
                host=self.host, port=self.port, CustomHandler=CustomHandler
            )

    # def fetch_origin(self):
    #     if not self.isResource_host:
    #         response = self.connection.get(request_data="LocalResources")
    #         print(response)
    #         self.LocalResources = response

    def read(self, read_variable: str):
        if self.isResource_host:
            if read_variable in self.LocalResources:
                return self.LocalResources[read_variable]
            else:
                return f"{read_variable} is Not Find"
        else:
            response = self.connection.RemoteResources_Access(
                method="READ", read_variable=read_variable
            )
            if response["status"] == "OK":
                return response["required_variable"]
            else:
                return f"{read_variable} is Not Find"

    def write(self, target_variable: str, value) -> bool:
        if self.isResource_host:
            self.LocalResources[target_variable] = value
            return True
        else:
            response = self.connection.RemoteResources_Access(
                method="WRITE", set_variable=target_variable, set_value=value
            )
            if response["status"] == "OK":
                return True
            else:
                return False
