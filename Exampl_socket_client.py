from easy_socket import SocketClient

# -----------------------------------------------------------------
# client
# -----------------------------------------------------------------


Connection = SocketClient(host="localhost")

response1 = Connection.request.get(request_data="price")  # 資源にアクセスしその値をgetする
response2 = Connection.request.post({"win": "tarou"})


print(response1)
print(response2)
