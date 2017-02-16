#!/usr/bin/python
import logging

class MPLogger(logging.Logger):
	def __init__(self, name):
		logging.Logger.__init__(self, logging.INFO)
		
		handler = logging.FileHandler("/tmp/"+ name + ".log")
		formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		handler.setFormatter(formatter)

		self.addHandler(handler)
	
'''
logger = MPLogger()
logger.info("Test my own logger")
'''