from graphics import *
import math
import re

ori=[int(x) for x in (re.split(' ',input("Enter the x & y coordinates of centre as tuple:")))]
rad=int(input("Enter radius:"))
xc=ori[0]
yc=ori[1]
pt=[]


for x in range(xc-rad,xc+rad):
    y=math.floor(math.sqrt(abs(rad*rad-(x-xc)*(x-xc)))+yc)
    pt.append(Point(x,y))
    y=2*yc-y
    pt.append(Point(x,y))

win=GraphWin('Circle Drawing',1000,800)

for p in pt:
    p.draw(win)

pc=Point(xc,yc)
pc.draw(win)

