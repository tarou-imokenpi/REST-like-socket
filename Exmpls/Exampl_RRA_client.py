from REST_like_socket import SocketClient


connection = SocketClient(host="localhost")

response1 = connection.request.RemoteResources_Access(
    method="SET", set_variable="name", set_value="alice"
)

response2 = connection.request.RemoteResources_Access(
    method="READ", read_variable="name"
)


print(response1)
print(response2)
