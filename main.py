import os, sys
import selectors
from daemon import MyDaemon


if __name__ == "__main__":
	daemon = MyDaemon("/home/lanthree/Tmp/python/connsvr/daemon.pid")
	if len(sys.argv) >= 2:
		if "start" == sys.argv[1]:
			daemon.start()
		elif "stop" == sys.argv[1]:
			daemon.stop()	
		else:
			print("wrong cmd")
	else:
		print("python3 main.py start|stop")
