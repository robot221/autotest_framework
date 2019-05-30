# -*- coding:utf-8 -*-

import logging,time,os.path

class Logger(object):
    def __init__(self,logger):

        '''
            指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        '''
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        dir_path = os.path.dirname(os.path.abspath('.')) + '/logs/'
        rq = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        logFile = dir_path + rq + '.log'
        fh = logging.FileHandler(logFile)
        fh.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s:%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
    def getlog(self):
        return self.logger
