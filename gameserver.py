import socket
import selectors
import time
import os
import log

def create_listener(host, port):
	
	listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	listener.bind((host, port))
	listener.listen(10)
	listener.setblocking(False)
	
	return listener

def runloop(listener):

	svr_log = log.getchannel_svr_log("gs:%d" % (os.getpid()))
	svr_log.info("gameserver get into function:runloop")
	
	selector	= selectors.DefaultSelector()
	selector.register(listener, selectors.EVENT_READ)

	while True:
		event_list	= selector.select()
		for key, events in event_list:
			conn = key.fileobj
			if conn == listener:
				new_conn, addr = conn.accept()
				new_conn.setblocking(False)
				selector.register(new_conn, selectors.EVENT_READ)
			else:
				message = conn.recv(1024)
				if message:
					svr_log.info("recv message:%s", message)
					conn.send(message)
				else:
					svr_log.info("recv over")
					selector.unregister(conn)
					conn.close()
