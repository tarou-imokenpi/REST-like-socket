import json
import socketserver
from socketserver import BaseRequestHandler
from threading import Thread


class ServerRequestHandler(BaseRequestHandler):
    def set_LocalResource(self):
        self.LocalResources: dict = dict()

    def check_RemoteResource(self):
        if not isinstance(self.LocalResources, dict):
            self.LocalResources: dict = {}
            raise (TypeError)

    def if_Post(self, posted_data):
        """POSTメソッドの処理

        Parameters
        ----------
        data : dict
            POSTリクエストで受信したデータ

        """
        pass

    def if_Get(self, requested_data):
        """GETメソッドの処理

        Parameters
        ----------
        data : dict
            GETリクエストで受信したデータ

        """
        pass

    def if_RemoteResources_Access(self, method):
        if method == "WRITE":
            self.set_variable = self.json_data["set_variable"]
            self.LocalResources[self.set_variable] = self.json_data["set_value"]
            self.send_response({"status": "OK"})

        elif method == "SET":
            self.set_variable = self.json_data["set_variable"]
            if self.find_variable(self.set_variable):
                self.LocalResources[self.set_variable] = self.json_data["set_value"]
                self.send_response({"status": "OK"})
            else:
                self.send_response(
                    {"status": "error", "mesaage": "Cannot find this variable."}
                )

        elif method == "NEW":
            self.set_variable = self.json_data["set_variable"]
            if not self.find_variable(self.set_variable):
                self.LocalResources[self.set_variable] = self.json_data["set_value"]
                self.send_response({"status": "OK"})
            else:
                self.send_response(
                    {"status": "error", "mesaage": "This variable is already set."}
                )

        elif method == "READ":
            self.read_variable = self.json_data["read_variable"]
            if self.find_variable(self.read_variable):
                response = self.LocalResources[self.read_variable]
                self.send_response({"status": "OK", "required_variable": response})
            else:
                self.send_response({"status": "error Not found"})

        else:
            self.send_response({"status": "error Not found method"})

    def find_variable(self, target_variable):
        if target_variable in self.LocalResources:
            return True
        else:
            return False

    def custom_HandleEvent(self, bytes_data: bytes, decoded_data: str, json_data: dict):
        """接続を受けたときの通常のハンドルにさらにオプションを加えたい場合に使用

        Parameters
        ----------
        bytes_data : bytes
            受信したbytes_data
        decoded_data : str
            受信したdecoded_data
        json_data : dict
            受信したjson_data
        """
        pass

    def get_client_address(self, client_address):
        """クライアントのアドレス情報を取得するメソッド
        Parameters
        ----------
        address : str
            クライアントのIPアドレス

        """
        pass

        self.set_LocalResource()
        self.check_RemoteResource()

    def handle(self):
        self.get_client_address(self.client_address[0])
        try:
            self.bytes_data: bytes = self.request.recv(4096).strip()
            self.decoded_data: str = self.bytes_data.decode()
            self.json_data: dict = json.loads(self.decoded_data)

            if "GET" in self.json_data:
                self.if_Get(self.json_data["GET"])
            elif "POST" in self.json_data:
                self.if_Post(self.json_data["POST"])
            elif "RRA" in self.json_data:
                self.if_RemoteResources_Access(self.json_data["RRA"])
            else:
                self.send_response("method error")

            self.custom_HandleEvent(self.bytes_data, self.decoded_data, self.json_data)

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            self.send_response("JSON decode error")

    def send_response(self, message) -> None:
        """レスポンスを送信するメソッド

        Parameters
        ----------
        message : str, optional
            送信するメッセージ

        Raises
        ------
        TypeError
            message引数が設定されていない場合

        """
        send_data = json.dumps(message)
        send_data: bytes = bytes(send_data, encoding="utf-8")
        self.request.sendall(send_data)

    # def send_bytes(self, bytes_data):
    #     self.request.sendall(bytes_data)


def Server(host="localhost", port=60000, CustomHandler=ServerRequestHandler) -> Thread:
    """サーバーの設定

    Parameters
    ----------
    host : host name, optional
        外部アクセスには 0.0.0.0
    port : int, optional
        port number, by default 9999
    CustomHandler : _type_, optional
        ServerRequestHandlerを継承したCustomHandler, by default ServerRequestHandler

    Returns
    -------
    Thread
        .start()で起動
    """

    def set_TCPServer():
        """TCPサーバーを設定し起動する"""
        with socketserver.TCPServer((host, port), CustomHandler) as server:
            print("start server")
            server.serve_forever()

    return Thread(target=set_TCPServer, daemon=True)
