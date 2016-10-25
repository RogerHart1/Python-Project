import graphics
from graphics import *
from time import *

window = GraphWin('DAT505 Graphics', 600, 600)
window.setBackground('pink3')

def function(value):
	cir1 = Circle(Point(42,100), value)
	cir1.setFill("yellow")
	cir1.setOutline("black")
	cir1.setWidth(1)
	cir1.draw(window)


text_file = open("data.txt")
lines = text_file.readlines()
data = []
for value in lines:
	data.append(int(value))

for value in data:

	#if value  < 50: 
		#print value
		#print " yes"
		function(value)
		sleep(1)










#function()
window.getMouse()
