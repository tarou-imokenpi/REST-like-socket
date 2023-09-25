from easy_socket import Server, SocketClient, ServerRequestHandler


# TODO: GlobalResource(リアルタイムでサーバーとクライアントで変更できる変数の辞書)を実装する


# この資源にGETリクエストでアクセスする
class Resources:
    global_variable: dict = {}


resources = Resources()
resources.global_variable["price"] = 100


# -------------------------------------------------------------
# server
# -------------------------------------------------------------
class CustomHandler(ServerRequestHandler):
    # Socket rules: 1 response per request
    def if_Post(self, posted_data):
        # postのときの処理
        print(f"data: {posted_data}")

        self.send_response({"request": "OK"})

    def if_Get(self, requested_data):
        if requested_data in resources.global_variable:
            self.send_response(
                {
                    "request": "OK",
                    "resources": resources.global_variable[requested_data],
                }
            )
        else:
            self.send_response({"request": "error"})

        # getのときの処理
        print(f"get:{requested_data}")

    def get_client_address(self, client_address):
        """リクエストされたipアドレスの処理"""

        # print(f"address:{address}")
        pass


server = Server(host="localhost", CustomHandler=CustomHandler)
server.start()


# -----------------------------------------------------------------
# client
# -----------------------------------------------------------------
Connection = SocketClient(host="localhost")

response1 = Connection.request.get(request_data="price")  # 資源にアクセスしその値をgetする
response2 = Connection.request.post({"win": "tarou"})
# -----------------------------------------------------------------
# -----------------------------------------------------------------


print(response1)
print(response2)

# Threadで動かしてるので終了いないようにjoinしておく
# severはdaemon=True なのでメインスレッドが終了するとserverも終了します。
server.join()
