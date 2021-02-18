import socket
import threading
import random

max_clients = 5
thread_pool = []
portList = []

for i in range(max_clients): portList.append(random.randint(1001,9999))

def director():
    global portList
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = '127.0.0.1'
    port = 1000

    s.bind((host, port))

    while True:
        s.listen()
        c, addr = s.accept()
        message = str(portList.pop(0)).encode('utf-8') if len(portList) > 0 else ("err".encode('utf-8'))
        c.sendall(message)

def receiver(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = '127.0.0.1'

    s.bind((host, port))

    s.listen()
    c, addr = s.accept()

    while True:
        r = c.recv(1024)
        if not r:
            continue
        c.sendall(r)

thread_pool.append(threading.Thread(target=director, daemon=True))

for i in range(max_clients):
    thread_pool.append(threading.Thread(target=receiver, daemon=True, kwargs={'port': portList[i]}))
    thread_pool.append(threading.Thread(target=sender, daemon=True, kwargs={'port': portList[i]}))

for thread in thread_pool:
    thread.start()

for thread in thread_pool:
    thread.join()