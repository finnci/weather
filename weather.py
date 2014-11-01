


import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto("YOUR-API-KEY.foo 1.2\n", ("carbon.hostedgraphite.com", 2003))
