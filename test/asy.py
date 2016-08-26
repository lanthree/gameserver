import asyncio

class EchoProtocol(asyncio.Protocol):
	def connection_made(self, transport):
		self.transport	= transport

	def connection_lost(self, exc):
		self.transport.close()

	def data_received(self, data):
		self.transport.write(data)

def server(host, port):
	loop	= asyncio.get_event_loop()
	srv		= loop.create_server(EchoProtocol, host, server)
	asyncio.async(srv)
	loop.run_forever()

