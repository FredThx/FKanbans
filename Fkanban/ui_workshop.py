# -*-coding:Latin-1 -*
from ui_object import *
from workshop import *
import Tkinter
import logging

class ui_workshop(Tkinter.Tk, workshop):
	''' a workshop with kanbans
	'''
	def __init__(self, parent, loops, name):
		workshop.__init__(self, name)
		self.parent = parent
		Tkinter.Tk.__init__(self, None)
		self.title(self.name)
		self.grid()
		column = 0
		for loop in loops:
			loop.ui_init(self, column, 0)
			column+=1			
		
		