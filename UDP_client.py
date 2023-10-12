import socket
import sys

HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])

# SOCK_DGRAM is the socket type to use for UDP sockets
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    # As you can see, there is no connect() call; UDP has no connections.
    # Instead, data is directly sent to the recipient via sendto().
    for _ in range(10):
        sock.sendto(bytes(data + "\n", "ascii"), (HOST, PORT))
        received = str(sock.recv(1024), "ascii")
        print(f"Sent:     {data}")
        print(f"Received: {received}")
