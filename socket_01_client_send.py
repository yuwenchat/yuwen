import socket


name = input("your name:")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("138.128.245.115", 39888))
    while True:
        text = input("message(< 10240 byte):")
        s.sendall(bytes(name+":"+text, "utf-8"))
