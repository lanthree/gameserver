import os, sys
import time
import selectors
import signal

import gameserver

from log	import sys_log
from daemon import Daemon
from conf	import conf


def handler(signum, frame):
	sys_log.info("monitor process[pid=%d] revc SIGTERM signal, notify child process exit", os.getpid())
	signal.signal(signal.SIGTERM, signal.SIG_IGN)
	os.kill(0, signal.SIGTERM)
	sys.exit(0)

def child_handler(signum, frame):
	sys_log.info("child process[pid=%d] recv SIGTERM signal, exit", os.getpid())
	sys.exit(0)

class GS_Controller(Daemon):

	def run(self):
		sys_log.info("monitor process[pid=%d] start function:run", os.getpid())

		signal.signal(signal.SIGCHLD, signal.SIG_DFL)
		signal.signal(signal.SIGTERM, handler)
		signal.signal(signal.SIGINT,  handler) # handle for test

		ip		= conf["ip"]
		port	= int(conf["port"]) 
		listener	= gameserver.create_listener(ip, port)
		sys_log.info("monitor process[pid=%d] get listener", os.getpid())

		process_num	= int(conf["process_num"])
		is_child = False

		while not is_child:
			if process_num > 0:
				try:
					pid = os.fork()
					if pid > 0:
						sys_log.info("create child process[pid=%d] ok", pid)
						process_num -= 1
					else:
						is_child = True			
				except OSError as e:
					sys_log.error("fork failed: %d (%s)\n" % (e.errno, e.strerror))
					sys.exit(1)
			else:
				try:
					pid, status	= os.wait()
					process_num += 1
					sys_log.error("monitor process pid=%d exit", pid)
				except OSError as e:
					sys_log.error("fork failed: %d (%s)\n" % (e.errno, e.strerror))
					sys.exit(1)

		if not is_child:
			sys_log.info("main process exit")
			os.kill(0, signal.SIGTERM)
			sys.exit(0)

		if is_child:
			signal.signal(signal.SIGTERM, child_handler)
			signal.signal(signal.SIGINT,  signal.SIG_IGN) # handle for test
			gameserver.runloop(listener)	
				
if __name__ == "__main__":
	
	gs_controller = GS_Controller(os.path.abspath(".") + "/daemon.pid")

	if len(sys.argv) >= 2:
		if "start" == sys.argv[1]:
			gs_controller.start()
		elif "stop" == sys.argv[1]:
			gs_controller.stop()
		elif "test" == sys.argv[1]:
			gs_controller.run()
		else:
			print("wrong cmd")
	else:
		print("python3 main.py [start|stop]")

