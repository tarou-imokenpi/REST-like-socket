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

        if self.isResource_host:
            self.server = Server(
                host=self.host, port=self.port, CustomHandler=CustomHandler
            )

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
