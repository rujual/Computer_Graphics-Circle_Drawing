from graphics import *
import math
import re

p1=[int(x) for x in (re.split(' ',input("Enter the x & y coordinates of start point as tuple:")))]
p2=[int(x) for x in (re.split(' ',input("Enter the x & y coordinates of end point as tuple:")))]

l=Line(Point(p1),Point(p2))

win=GraphWin('Line Clipping',1000,800)
l.draw(win)

