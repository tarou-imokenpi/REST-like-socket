import json
import socket
from typing import Literal


def socket_connect(data, request_method=None) -> dict:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self_HOST, self_PORT))
            if request_method:
                send_data = {request_method: data}
            else:
                send_data = data
            send_data_json = json.dumps(send_data)
            send_data: bytes = bytes(send_data_json, encoding="utf-8")
            sock.sendall(send_data)
            response = str(sock.recv(4096), encoding="utf-8")
            return json.loads(response)
    except ConnectionRefusedError:
        return {"status": "ConnectionRefusedError"}


class SocketClient:
    def __init__(self, host="localhost", port: int = 60000) -> None:
        global self_HOST
        global self_PORT
        self_HOST, self_PORT = host, port

    class request:
        def get(request_data: str):
            return socket_connect(request_method="GET", data=request_data)

        def post(self, post_data):
            return socket_connect(request_method="POST", data=post_data)

        def RemoteResources_Access(
            method: Literal["SET", "READ", "NEW"],
            set_variable: str = None,
            read_variable: str = None,
            set_value=None,
        ) -> dict:
            if method == "SET" or method == "NEW":
                send_data = {
                    "RRA": method,
                    "set_variable": set_variable,
                    "set_value": set_value,
                }
            else:
                send_data = {
                    "RRA": method,
                    "read_variable": read_variable,
                }
            return socket_connect(data=send_data)
