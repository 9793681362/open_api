import logging
import os.path
import datetime
from os import path

def get_logger(log_name ):
    logger = logging.getLogger(log_name) # 创建日志器
    sh = logging.StreamHandler()  # 创建控制台处理器
    sh.setFormatter(logging.Formatter('%(asctime)s|%(levelname)s|%(message)s')) # 格式器
    logger.addHandler(sh) # 将日志信息输出到控制台
    log_path = path.abspath('./log')  # 文本log,当前项目下创建log文件

    # 进入log路径，写入信息
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    log_path = os.path.join(log_path,'%s.log' % log_name)
    if not os.path.exists(log_path):
        open(log_path,'w')

    fh = logging.FileHandler(log_path,encoding='utf-8')
    fh.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(filename)s[%(lineno)d] - %(message)s'))
    logger.addHandler(fh)
    logger.setLevel(20) # logger等级
    return logger

run_time = 'runtime_' + str(datetime.datetime.now().strftime("%Y%m%d")) # 构建日志return_xxx.log的名称
debugLogger = get_logger(log_name=run_time)

log = debugLogger
if __name__ == '__main__':
    log.debug("这是一条debug日志信息")
    log.info("这是一条info日志信息")
    log.warning("这是一条warning日志信息")
    log.error("这是error信息")
    log.critical("这是一条critical日志信息")
