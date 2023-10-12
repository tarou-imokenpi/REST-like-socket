from REST_like_socket import SocketClient


connection = SocketClient(host="localhost")

response1 = connection.RemoteResources_Access(
    method="WRITE", set_variable="name", set_value="alice"
)


print(f"response1: {response1}")
