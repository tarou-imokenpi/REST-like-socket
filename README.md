# REST-like-socket
RESTライクなGETとPOSTの概念を取り入れたsocket通信ライブラリです。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

## install
正式リリースではありませんが、実験的に試すことが出来ます。
```bash
pip install -i https://test.pypi.org/simple/ REST-Like-Socket
```
## Usage
外部に公開したい場合は`host`を"0.0.0.0"に設定してください。
### client
```python
from REST_like_socket import SocketClient


connection = SocketClient(host="localhost")

response1 = connection.request.get(request_data="apple_price")
response2 = connection.request.post(100)


print(response1)
print(response2)
```
### server

```python
from REST_like_socket import Server, ServerRequestHandler


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
# High Level API SyncedResources
ホストとクライアント間で同期された変数が簡単に使用できます。
### host
```python
from REST_like_socket import SyncedResources


syncedResources = SyncedResources(isResource_host=True)
syncedResources.server.start()

syncedResources.write("num", 0)

apple_price= syncedResources.read("apple_price")
print(apple_price)


syncedResources.server.join()
```
### client
```python
from REST_like_socket import SyncedResources


syncedResources = SyncedResources(
    isResource_host=False,
    synchronize_to="X.X.X.X",
)

num = syncedResources.read("num")
print(num)


syncedResources.write("apple_price", 100)

```


## RemoteResources_Access
クライアントがサーバー側の変数の取得、更新、追加が出来ます。
### client
```python
from REST_like_socket import SocketClient


connection = SocketClient(host="localhost")

response1 = connection.request.RemoteResources_Access(
    method="SET", set_variable="name", set_value="alice"
)

response2 = connection.request.RemoteResources_Access(
    method="READ", read_variable="name"
)


print(response1) # >>> {'status': 'OK', 'method': 'SET'}
print(response2) # >>> {'status': 'OK', 'required_variable': 'alice'}

```
### server
```python
from REST_like_socket import Server, ServerRequestHandler


RemoteResources = dict(
    {
        "name": "tarou",
    }
)


class CustomHandler(ServerRequestHandler):
    # リモートでアクセスできる資源を指定します。
    def set_RemoteResource(self):
        self.RemoteResources: dict = RemoteResources


server = Server(host="localhost", CustomHandler=CustomHandler)
server.start()

server.join()
```
### RemoteResources_Access 引数について

| 引数名       | 型                                     | 説明                                                             |
|--------------|---------------------------------------|------------------------------------------------------------------|
| method       | Literal["SET", "READ", "NEW"]       | アクセスメソッドを指定します。                                        |
| set_variable | str                  | セットまたは新しいリモートリソースを指定するための変数名。 `method` が "SET" または "NEW" の場合に使用されます。 |
| read_variable | str                                | リモートリソースから読み取る変数名。 `method` が "READ" の場合に使用されます。     |
| set_value    | 任意の型                              | `method` が "SET" または "NEW" の場合に設定される値。                           |
