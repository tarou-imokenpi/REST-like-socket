from easy_socket import Server, ServerRequestHandler


class Resources:
    global_variable: dict = {}


resources = Resources()
resources.global_variable["price"] = 100


# -------------------------------------------------------------
# server
# -------------------------------------------------------------


class CustomHandler(ServerRequestHandler):
    # Socket rules: 1 response per request
    def if_Post(self, post_data):
        # postのときの処理
        print(f"data: {post_data}")

        self.send_response({"request": "OK"})

    def if_Get(self, request_data):
        if request_data in resources.global_variable:
            self.send_response(
                {
                    "request": "OK",
                    "resources": resources.global_variable[request_data],
                }
            )
        else:
            self.send_response({"request": "error"})

        # getのときの処理
        print(f"get:{request_data}")

    def get_client_address(self, address):
        """リクエストされたipアドレスの処理"""

        # print(f"address:{address}")
        pass


server = Server(host="localhost", CustomHandler=CustomHandler)
server.start()

server.join()
