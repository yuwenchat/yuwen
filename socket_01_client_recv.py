import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("138.128.245.115", 39888))
    while True:
        data = s.recv(1024)
        print(str(data, "utf-8"))
