import socket

host = '127.0.0.1'
port = 1000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

while True:
    r = s.recv(1024).decode('utf-8')

    if r:
        port = int(r)
    
    break

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

while True:
    r = s.recv(1024).decode('utf-8')
    if r:
        print(r)