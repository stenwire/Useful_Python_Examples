import socket
hostname = socket.gethostname()
ipAddr = socket.gethostbyname(hostname)
print(ipAddr)


