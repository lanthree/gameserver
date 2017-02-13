#coding utf-8

import socket
import selectors
import sys

to_addr = ('127.0.0.1', 30008)
fr_addr = ('', 30007)

class Proxy:
	def __init__(self):
		self.proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.proxy.bind(fr_addr)
		self.proxy.listen(10);
		self.route  = {}

	def serve_forever(self):
		print('proxy listen')

		self.selector = selectors.DefaultSelector()
		self.selector.register(self.proxy, selectors.EVENT_READ)

		while True:
			event_list = self.selector.select()
			for key, events in event_list:
				self.sock = key.fileobj
				if self.sock == self.proxy:
					self.on_join()
				else:
					data = self.sock.recv(8096)
					if not data:
						self.on_quit()
					else:
						self.route[self.sock].send(data)
	
	def on_join(self):
		client, addr = self.proxy.accept()
		print(addr, 'connect')
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.connect(to_addr)

		self.selector.register(client, selectors.EVENT_READ)
		self.selector.register(server, selectors.EVENT_READ)

		self.route[client] = server
		self.route[server] = client

	def on_quit(self):
		for s in self.sock, self.route[self.sock]:
			self.route.pop(s)
			self.selector.unregister(s)
			s.close()

if __name__ == '__main__':
	try:
		Proxy().serve_forever()
	except KeyboardInterrupt:
		sys.exit(1)

