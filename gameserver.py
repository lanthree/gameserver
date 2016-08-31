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
	
	while True:
		time.sleep(1)
		svr_log.debug("runloop sleep 1sec")
