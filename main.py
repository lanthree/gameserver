import os, sys
import time
import selectors

from daemon import Daemon
from conf	import conf
from log	import sys_log, svr_log

class GS_Controller(Daemon):

	def run(self):
		print(conf)
		
		ip		= conf["ip"]
		port	= int(conf["port"]) 
		process_num	= int(conf["process_num"])
		is_child = False

		while not is_child:
			if process_num > 0:
				try:
					pid = os.fork()
					if pid > 0:
						sys_log.info("create child process pid=%d ok", os.getpid())
						process_num -= 1
					else:
						is_child = True			
				except OSError as e:
					sys_log.error("fork #1 failed: %d (%s)\n" % (e.errno, e.strerror))
					sys.exit(1)
			else:
				break		
				
				
		

if __name__ == "__main__":
	
	gs_controller = GS_Controller(os.path.abspath(".") + "/daemon.pid")

	if len(sys.argv) >= 2:
		if "start" == sys.argv[1]:
			server.start()
		elif "stop" == sys.argv[1]:
			server.stop()
		elif "test" == sys.argv[1]:
			gs_controller.run() 
		else:
			print("python3 main.py [start|stop|test]")
	else:
		print("python3 main.py [start|stop|test]")

