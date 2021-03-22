import socket
from oled_show import t, h
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.0.165', 8888))
#t = datetime.strftime(%Y)
sock.send(b'TEST MSG')
t = bytes(t, 'utf8')
h = bytes(h, 'utf8')
sock.send(t, h)

res = sock.recv(1024)
#print(t)
print('ANSWER', res.decode())
sock.close()

