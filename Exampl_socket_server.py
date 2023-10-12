from REST_like_socket import Server, ServerRequestHandler


# -------------------------------------------------------------
# server
# -------------------------------------------------------------


class CustomHandler(ServerRequestHandler):
    # Socket rules: 1 response per request

    def if_Get(self, requested_data):
        self.send_response({"request": "OK", "meaage": "hello !!!!!!!!!!!"})
        # getのときの処理
        print(f"get:{requested_data}")

    def get_client_address(self, client_address):
        """リクエストされたipアドレスの処理"""

        print(f"from :{client_address}")


server = Server(host="0.0.0.0", port=55555, CustomHandler=CustomHandler)
server.start()

server.join()
