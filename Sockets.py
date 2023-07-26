import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1',12345))
server_socket.listen(1) #for limiting the number of clients
client,adress=server_socket.accept()
print(f"Connected Adress is:{adress}")
data=client.recv(1024)
print(f"recieved data {data.decode()}")

