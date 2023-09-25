# easy-socket
RESTライクなGETとPOSTの概念を取り入れたsocket通信ライブラリです。
## Usage

### client
```python
from easy_socket import SocketClient


connection = SocketClient(host="localhost")

response1 = connection.request.get(request_data="apple_price")
response2 = connection.request.post(100)


print(response1)
print(response2)
```
### server

```python
from easy_socket import Server, ServerRequestHandler


class CustomHandler(ServerRequestHandler):
    # Socket rules: 1リクエストにつき1レスポンス

    def if_Get(self, requested_data):
        # getのされたの処理
        self.send_response({"request": "OK"})

    def if_Post(self, posted_data):
        # postされたとき処理
        result = int(posted_data) * 2
        self.send_response({"request": "OK","result":result})




server = Server(host="localhost", CustomHandler=CustomHandler)
server.start()

server.join()

```

外部に公開したい場合は`host`を"0.0.0.0"に設定してください。