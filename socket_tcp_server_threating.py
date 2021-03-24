import socketserver
from time import strftime as time

class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class TCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024).strip()
        time_ = time('%d - %m - %Y, %X')
        print(time_)
        print('Addr::{}/ {}'.format(self.client_address[0], self.client_address[1]))
        print('Data:{}'.format(data.decode()))
        self.request.sendall(data)
        self.request.sendall(bytes(time_, 'utf8'))

if __name__ == '__main__':
    with ThreadingTCPServer(('', 8888), TCPHandler) as server:
        server.serve_forever()
