import socket

sock	= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect( ("192.168.237.128", 8888) )

cnt = 1
now = 0
while now < cnt:
	sock.send(b"test")
	now += 1

sock.setblocking(False)
while True:
	try:
		message = sock.recv(1024)
		if message:
			print(message)
		else:
			break
	except BlockingIOError as e:
		break

sock.close()
