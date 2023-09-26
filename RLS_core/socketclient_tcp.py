import json
import socket
from typing import Literal


class SocketClient:
    def __init__(self, host="localhost", port: int = 60000) -> None:
        self.HOST, self.PORT = host, port

    def socket_connect(self, data, request_method=None) -> dict:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((self.HOST, self.PORT))
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

    def get(self, request_data: str):
        return self.socket_connect(request_method="GET", data=request_data)

    def post(self, post_data):
        return self.socket_connect(request_method="POST", data=post_data)

    def RemoteResources_Access(
        self,
        method: Literal["WRITE", "SET", "NEW", "READ"],
        set_variable: str = None,
        set_value: any = None,
        read_variable: str = None,
    ) -> dict:
        """サーバの変数にアクセスします。

        Parameters
        ----------
        method : Literal
            "WRITE": 指定した変数を更新します、定義されていない場合は新しく作成します\n
            "SET"  : 指定した変数を更新します\n
            "NEW"  : 指定した変数が定義されていない場合は新しく作成します\n
            "READ" : 指定した変数を読み取ります\n
        set_variable : str, optional
            メソッドが "SET"、"NEW"、または "WRITE "の場合に使用可能, by default None\n
        set_value : _type_, optional
            メソッドが "SET"、"NEW"、または "WRITE "の場合に使用可能, by default None\n
        read_variable : str, optional
            メソッドが "READ"の場合に使用可能, by default None\n
        Returns
        -------
        dict
            "WRITE" or "SET" "NEW"
            return dict key >>>  "status"

            "READ"
            return dict key >>>  "status" and "required_variable"
            ""
        """
        if method == "SET" or method == "NEW" or method == "WRITE":
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
        return self.socket_connect(data=send_data)
