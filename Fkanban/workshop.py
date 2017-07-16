# -*-coding:Latin-1 -*

class workshop(object):
	''' a workshop with kanbans
	'''
	def __init__(self, name):
		'''Initialisation
			- name
		'''
		self.name = name
	
	def __str__(self):
		return self.name
