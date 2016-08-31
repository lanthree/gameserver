import logging

# 配置日志信息
logging.basicConfig(
    level=logging.DEBUG,
    #format='[%(asctime)s] [%(levelname)s] [@ %(filename)s line:%(lineno)d] [channel:%(name)s] %(message)s',
    #datefmt='%m-%d %H:%M',
    filename='/dev/null',
    #filemode='w')
    )

# ---------------------------sys_log---------------------------
sys_log_handler		= logging.FileHandler("./log/sys.log", "w")
sys_log_formatter	= logging.Formatter("[%(asctime)s] [%(levelname)s] [@ %(filename)s line:%(lineno)d] %(message)s")
sys_log_handler.setLevel(logging.INFO)
sys_log_handler.setFormatter(sys_log_formatter)

logging.getLogger("sys_log").addHandler(sys_log_handler)
sys_log	= logging.getLogger('sys_log')
# ---------------------------sys_log---------------------------

# ---------------------------svr_log---------------------------
channel_svr_log = {}
def getchannel_svr_log(channel):
	
	channel = str(channel)
	if not channel in channel_svr_log:

		svr_log_handler		= logging.FileHandler("./log/" + channel + ".log", "w")
		svr_log_formatter	= logging.Formatter("[%(asctime)s] [%(levelname)s] [@ %(filename)s line:%(lineno)d] [%(name)s] %(message)s")
		svr_log_handler.setLevel(logging.INFO)
		svr_log_handler.setFormatter(svr_log_formatter)

		logging.getLogger(channel).addHandler(svr_log_handler)
		channel_svr_log[channel] = logging.getLogger(channel)
	
	return channel_svr_log[channel]
# ---------------------------svr_log---------------------------
