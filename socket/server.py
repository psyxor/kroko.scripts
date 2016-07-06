# -*- coding: utf-8 -*-
import socket
sock = socket.socket()
sock.bind(('',10000))
sock.listen(2)
conn, addr = sock.accept()
print u"Геннадий с адресом: ", addr, u" подключился"
while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send("Success")
    print data
