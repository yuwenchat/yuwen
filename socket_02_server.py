import os
import socket


def handle_client(c, addr, root):
    print("{}connected.".format(addr))
    with c:
        request = c.recv(10240)
        headers = request.split(b"\r\n")
        file = headers[0].split()[1].decode()

        if file == "/" or file == "http://138.128.245.115/" or file == "http://138.128.245.115:39555/":
            file = "/index.html"
        print(root)
        print(file)

        try:
            with open(root + file, "rb") as f:
                content = f.read()
            res = b"HTTP/1.0 200 OK\r\n\r\n" + content

        except FileNotFoundError:
            with open(root + "/404.html", "rb")as f:
                content = f.read()
            res = b"HTTP/1.0 404 NOT FOUND\r\n\r\n" + content

        c.sendall(res)


if __name__ == '__main__':
    # os.chdir()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("0.0.0.0", 39555))
        s.listen()

        while True:
            c, addr = s.accept()
            handle_client(c, addr, os.path.dirname(os.path.abspath(__file__)))
