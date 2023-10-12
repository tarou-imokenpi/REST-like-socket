from REST_like_socket import Server, ServerRequestHandler


RemoteResources = dict(
    {
        "name": "tarou",
        "point": 0,
    }
)


class CustomHandler(ServerRequestHandler):
    # リモートでアクセスできる資源を指定します。
    def set_LocalResource(self):
        self.LocalResources: dict = RemoteResources

    def if_Get(self, requested_data):
        self.send_response("aaaa")

    # 接続を受けたときの通常のハンドルにさらにオプションを加えたい場合に使用
    def custom_HandleEvent(self, bytes_data: bytes, decoded_data: str, json_data: dict):
        # 受信した内容を表示
        print(json_data)


server = Server(host="0.0.0.0", port=55555, CustomHandler=CustomHandler)
server.start()

server.join()
