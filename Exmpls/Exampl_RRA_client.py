from REST_like_socket import SocketClient


connection = SocketClient(host="localhost")

response1 = connection.request.RemoteResources_Access(
    method="SET", set_variable="name", set_value="alice"
)
response2 = connection.request.RemoteResources_Access(
    method="READ", read_variable="name"
)
response3 = connection.request.RemoteResources_Access(
    method="READ", read_variable="new_variable_name"
)
response4 = connection.request.RemoteResources_Access(
    method="NEW", set_variable="new_variable_name", set_value=1000
)
response5 = connection.request.RemoteResources_Access(
    method="READ", read_variable="new_variable_name"
)

print(type(response2))

if response2["status"] == "OK":
    result = response2["required_variable"]
    print(f"result:{result}")


print(f"response1: {response1}")
print(f"response2: {response2}")
print(f"response3: {response3}")
print(f"response4: {response4}")
print(f"response5: {response5}")
