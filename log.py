import logging

# 配置日志信息
logging.basicConfig(
    level=logging.DEBUG,
    #format='[%(asctime)s] [%(levelname)s] [@ %(filename)s line:%(lineno)d] [channel:%(name)s] %(message)s',
    #datefmt='%m-%d %H:%M',
    filename='/dev/null',
    #filemode='w')
    )


# ------------myapp.area1 logger--------------
log3 = logging.FileHandler("test.log", "w")
log3.setLevel(logging.DEBUG)
log3formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] [@ %(filename)s line:%(lineno)d] [channel:%(name)s] %(message)s')
log3.setFormatter(log3formatter)
logging.getLogger("myapp.area1").addHandler(log3)
# ------------myapp.area1 logger--------------


logger1 = logging.getLogger('myapp.area1')
logger2 = logging.getLogger('myapp.area2')

logger1.debug('Quick zephyrs blow, vexing daft Jim.')
logger1.info('How quickly daft jumping zebras vex.')
logger2.warning('Jail zesty vixen who grabbed pay from quack.')
logger2.error('The five boxing wizards jump quickly.')
