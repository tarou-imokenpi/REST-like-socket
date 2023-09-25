import json
import socketserver
from socketserver import BaseRequestHandler
from threading import Thread


class ServerRequestHandler(BaseRequestHandler):
    def if_Post(self, post_data):
        """POSTメソッドの処理

        Parameters
        ----------
        data : dict
            POSTリクエストで受信したデータ

        """
        pass

    def if_Get(self, request_data):
        """GETメソッドの処理

        Parameters
        ----------
        data : dict
            GETリクエストで受信したデータ

        """
        pass

    def get_client_address(self, address):
        """クライアントのアドレス情報を取得するメソッド
        Parameters
        ----------
        address : str
            クライアントのIPアドレス

        """
        pass

    def handle(self):
        """
        TODO:リモート資源にアクセスできるようにする
        """
        # 受信
        try:
            self.get_client_address(self.client_address[0])
            self.data: bytes = self.request.recv(4096).strip()
            self.data: str = self.data.decode()
            self.data: dict = json.loads(self.data)
            if "POST" in self.data:
                self.if_Post(self.data["POST"])

            elif "GET" in self.data:
                self.if_Get(self.data["GET"])

            else:
                self.send_response("method error")

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            self.send_response("JSON decode error")

        self.get_client_address(self.client_address[0])

    def send_response(self, message=None) -> None:
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
        try:
            data = str(message)
            send_data: bytes = bytes(data, encoding="utf-8")
            self.request.sendall(send_data)
        except TypeError:
            print("エラーが発生しました。")
            print("--------message引数を設定してください---------")

    # def send_bytes(self, bytes_data):
    #     self.request.sendall(bytes_data)


def Server(host="0.0.0.0", port=60000, CustomHandler=ServerRequestHandler) -> Thread:
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
