'''
Created on 22 Jan 2014

@author: corrupted
'''
import logging, datetime
from logging import handlers

def fixedtime(record, datefmt=None):
    try:
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]
    except:
        pass

def Log(LOG_FILENAME='/var/log/dynamic.log', init=False, name="ICMP"):
    try:
        logger = logging.getLogger(name)
        if init:
            logger.setLevel(logging.DEBUG)
            bf = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            bf.formatTime = fixedtime
            handler = handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=20971520, backupCount=5)
            logger.addHandler(handler)
            handler.setFormatter(bf)
        return(logger)
    except:
        raise
