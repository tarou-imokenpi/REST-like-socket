from REST_like_socket import SocketClient

# -----------------------------------------------------------------
# client
# -----------------------------------------------------------------


connection = SocketClient(host="localhost")

response1 = connection.get(request_data="price")  # 資源にアクセスしその値をgetする


print(response1)
