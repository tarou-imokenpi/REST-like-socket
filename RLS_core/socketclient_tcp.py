import json
import socket
from typing import Literal


class SocketClient:
    def __init__(self, host="localhost", port: int = 60000) -> None:
        global self_HOST
        global self_PORT
        self_HOST, self_PORT = host, port

    class request:
        def get(request_data: str):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.connect((self_HOST, self_PORT))
                    send_data = {"GET": request_data}
                    send_data_json = json.dumps(send_data)
                    send_data: bytes = bytes(send_data_json, encoding="utf-8")
                    sock.sendall(send_data)
                    response = str(sock.recv(4096), encoding="utf-8")
                    return response
            except ConnectionRefusedError:
                return "接続に失敗しました。"

        def post(post_data):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.connect((self_HOST, self_PORT))
                    send_data = {"POST": post_data}
                    send_data_json = json.dumps(send_data)
                    send_data: bytes = bytes(send_data_json, encoding="utf-8")
                    sock.sendall(send_data)
                    response = str(sock.recv(4096), encoding="utf-8")
                    return response
            except ConnectionRefusedError:
                return "接続に失敗しました。"

        def RemoteResources_Access(
            method: Literal["SET", "READ", "NEW"],
            set_variable: str = None,
            read_variable: str = None,
            set_value=None,
        ):
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
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.connect((self_HOST, self_PORT))
                    send_data_json = json.dumps(send_data)
                    send_data: bytes = bytes(send_data_json, encoding="utf-8")
                    sock.sendall(send_data)
                    response = str(sock.recv(4096), encoding="utf-8")
                    return response
            except ConnectionRefusedError:
                return {"ConnectionRefusedError"}
