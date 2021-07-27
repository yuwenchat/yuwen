import socket
import threading

user_list = {}


def handle_client(c, addr):
    print("{}connected.".format(addr))
    try:
        while True:
            data = c.recv(10240)
            print(str(data, "utf-8"))
            for ak, bk in user_list.items():
                bk.sendall(data)
    except:
        pass


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("0.0.0.0", 39888))
    s.listen()

    while True:
        c, addr = s.accept()

        t = threading.Thread(target=handle_client, args=(c, addr))
        t.start()
        user_list[t] = c
        for i in list(user_list.keys()):
            if not i.isAlive():
                del user_list[i]
        print(str(len(user_list))+"numbers connecting.")
