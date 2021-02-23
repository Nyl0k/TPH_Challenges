import socket
import threading
import random

max_clients = 5
socket_list = []
thread_pool = []

def director():
    global socket_list
    print("Initialized director")
    for [sock, p] in socket_list:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '127.0.0.1'
        port = 1000

        s.bind((host, port))
        while True:
            s.listen()
            c, addr = s.accept()
            break
        print("New connection")
        c.sendall(str(p).encode('utf-8'))
        s.close()

def sender(s):
    print("Initialized sender")
    while True:
        s.listen()
        c, _ = s.accept()
        break
    
    print("sending message")

    while True:
        c.sendall("a".encode('utf-8'))

for _ in range(max_clients):
    s = socket.socket()
    port = random.randint(1001,9999)
    s.bind(('127.0.0.1', port))
    socket_list.append([s, port])

thread_pool.append(threading.Thread(target=director, daemon=True))

for [s, p] in socket_list:
    thread_pool.append(threading.Thread(target=sender, daemon=True, kwargs={'s':s}))

for thread in thread_pool:
    thread.start()

while True:
    continue