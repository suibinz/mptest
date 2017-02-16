#!/usr/bin/python
import os
import logging
import datetime
import xmltodict
settingFile = "settings.xml"

class MPLogger(logging.Logger):
	def __init__(self, name):
		#setting the logging directory, filename format is fixed
		loc = os.environ["MPHOME"] + settingFile
		with open(loc, "r") as f:
			setting = xmltodict.parse(f.read())
		logdir = setting["mpSettings"]["logging"]["test_log_dir"]

		logging.Logger.__init__(self, logging.INFO)
		timeStr = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
		handler = logging.FileHandler(logdir + name + "-" + timeStr + ".log")
		formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		handler.setFormatter(formatter)

		self.addHandler(handler)
	
'''
logger = MPLogger()
logger.info("Test my own logger")
'''