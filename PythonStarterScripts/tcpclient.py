import socket

target_host = "127.0.0.1"
target_port = 4444

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # INET means Ipv4, SOCK_STREAM means tcp client

client.connect((target_host, target_port)) #connects the client

client.send("stuff")

response = client.recv(4096)

print response
