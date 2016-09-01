import socket
import selectors

def handler(conn, selector):
	message	= conn.recv(1024)
	if message:
		print(message)
		conn.send(message)
	else:
		print("recv over")
		selector.unregister(conn)
		conn.close()

def server(host, port):
	listener	= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	listener.bind((host, port))
	listener.listen(10)
	listener.setblocking(False)	

	selector	= selectors.DefaultSelector()
	selector.register(listener, selectors.EVENT_READ)

	while True:
		try:
			event_list	= selector.select()
		except OSERR as e:
			print(e)

		for key, events in event_list:
			conn = key.fileobj
			if conn == listener:
				new_conn, addr	= conn.accept()
				new_conn.setblocking(False)
				selector.register(new_conn, selectors.EVENT_READ)
			else:
				handler(conn, selector)

server("192.168.237.128", 8888)
