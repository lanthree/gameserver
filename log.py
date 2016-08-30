import logging

# 配置日志信息
logging.basicConfig(
    level=logging.DEBUG,
    #format='[%(asctime)s] [%(levelname)s] [@ %(filename)s line:%(lineno)d] [channel:%(name)s] %(message)s',
    #datefmt='%m-%d %H:%M',
    filename='/dev/null',
    #filemode='w')
    )

# ------------sys log--------------
sys_log_handler		= logging.FileHandler("./log/sys.log", "w")
sys_log_formatter	= logging.Formatter("[%(asctime)s] [%(levelname)s] [@ %(filename)s line:%(lineno)d] %(message)s")
sys_log_handler.setLevel(logging.INFO)
sys_log_handler.setFormatter(sys_log_formatter)

logging.getLogger("sys_log").addHandler(sys_log_handler)
# ------------sys log--------------

# ------------svr log--------------
svr_log_handler		= logging.FileHandler("./log/svr.log", "w")
svr_log_formatter	= logging.Formatter("[%(asctime)s] [%(levelname)s] [@ %(filename)s line:%(lineno)d] %(message)s")
svr_log_handler.setLevel(logging.INFO)
svr_log_handler.setFormatter(svr_log_formatter)

logging.getLogger("svr_log").addHandler(svr_log_handler)
# ------------svr log--------------

sys_log	= logging.getLogger('sys_log')
svr_log = logging.getLogger('svr_log')

