import socket
import multiprocessing

def handler(conn, addr):
	message	= conn.recv(1024)
	while message:
		conn.send(message)
		print(message)
	conn.close()

def server(host, port):
	listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	listener.bind((host, port))
	listener.listen(10)

	while True:
		conn, addr	= listener.accept()
		process		= multiprocessing.Process(target=handler, args=(conn, addr))
		process.start()
		process.join()

server("192.168.237.128", 8888);

