# -*- coding: utf-8 -*-
import sys, platform, os, socket
if platform.system() == "Windows": 
    d = platform.uname()
    if d[1] != "Username":
        print u"Вы что, совсем что-ли, Геннадий?"
    else:
        print u"OS:", d[0] + d[2]
        print u"Python verison:", platform.python_version()
        out = d[0] + d[2], platform.python_version(), d[1]
        sock = socket.socket()
        sock.connect(("127.0.0.1", 10000))
        deeep = " ".join(out)
        sock.send(deeep)
        data = sock.recv(1024)
        sock.close()
        print data
