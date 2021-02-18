import socket

host = '127.0.0.1'
port = 1000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

while True:
    s.sendall(input("Message: ").encode('utf-8'))
    r = s.recv(1024)

    print(f"Received {r.decode('utf-8')}")