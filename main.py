import os, sys
import time
import selectors

from daemon import Daemon
from conf import conf

class ServerCore(Daemon):
	def run(self):
		print(conf)
		while True:
			time.sleep(2)
			print('daemon runing') # be in log

if __name__ == "__main__":
	
	server = ServerCore(os.path.abspath(".") + "/daemon.pid")

	if len(sys.argv) >= 2:
		if "start" == sys.argv[1]:
			server.start()
		elif "stop" == sys.argv[1]:
			server.stop()	
		else:
			print("wrong cmd")
	else:
		print("python3 main.py start|stop")

