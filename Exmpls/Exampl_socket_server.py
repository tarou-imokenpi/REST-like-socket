from REST_like_socket import Server, ServerRequestHandler


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

server.join()
