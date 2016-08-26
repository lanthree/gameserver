import socket

sock	= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect( ("192.168.237.128", 9999) )

cnt = 100
now = 0
while now < cnt:
	sock.send(bytes("test", "utf-8"))
	now += 1

sock.setblocking(False)
while True:
	try:
		message = sock.recv(1024)
		print(message)
	except BlockingIOError as e:
		print(e)
		break

sock.close()
