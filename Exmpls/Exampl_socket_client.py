from REST_like_socket import SocketClient

# -----------------------------------------------------------------
# client
# -----------------------------------------------------------------


connection = SocketClient(host="localhost")

response1 = connection.request.get(request_data="price")  # 資源にアクセスしその値をgetする
response2 = connection.request.post("hello")


print(response1)
print(response2)
