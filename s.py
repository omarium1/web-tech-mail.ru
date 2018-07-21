import os
import sys
import socket

s = socket.socket()
s.bind(("0.0.0.0", 2222))
s.listen()

while True:
    conn, addr = s.accept()
    pid = os.fork()
    if pid == 0:
        data = conn.recv(1024)
        if not data: break
        conn.send(data)
        conn.close()
        sys.exit()
    else:
        conn.close()

s.close()
