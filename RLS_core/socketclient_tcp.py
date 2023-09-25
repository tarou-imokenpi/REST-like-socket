import json
import socket


class SocketClient:
    def __init__(self, host="localhost", port: int = 60000) -> None:
        global self_HOST
        global self_PORT
        self_HOST, self_PORT = host, port

    class request:
        """リクエストを送信してレスポンスを受信

        Parameters
        ----------
        method : Literal["POST", "GET"]
            送信するHTTPメソッド ("POST" または "GET")
        data : any
            送信するデータ

        Returns
        -------
        str
            サーバーからのレスポンスメッセージ

        """

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


# TCP_Connection = SocketClient(host="localhost", port=9999)


# response = TCP_Connection.request("POST", ["aaa", "bbb"])

# print(response)
