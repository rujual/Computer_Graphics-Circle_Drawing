from graphics import *
import math
import re

#def bresenhamcircledraw()
ori=[int(x) for x in (re.split(' ',input("Enter the x & y coordinates of centre as tuple:")))]
rad=int(input("Enter radius:"))
xc=ori[0]
yc=ori[1]
pt=[]

for x in range(int(xc+rad/math.sqrt(2)),xc+rad):
    y=math.sqrt(abs(rad*rad-(x-xc)*(x-xc)))+yc
    yl=math.floor(y)
    yh=math.ceil(y)
    ym=(yl+yh)/2
    t=((ym-yc)**2)+((x-xc)**2)-rad**2
    if(t>0):
        pt.append(Point(x,yl))
        pt.append(Point(2*xc-x,yl))
        pt.append(Point(x,2*yc-yl))
        pt.append(Point(2*xc-x,2*yc-yl))
    else:
        pt.append(Point(x,yh))
        pt.append(Point(2*xc-x,yh))
        pt.append(Point(x,2*yc-yh))
        pt.append(Point(2*xc-x,2*yc-yh))


for x in range(xc,int(xc+rad/math.sqrt(2))):
    y=math.sqrt(abs(rad*rad-(x-xc)*(x-xc)))+yc
    yl=math.floor(y)
    yh=math.ceil(y)
    ym=(yl+yh)/2
    t=((ym-yc)**2)+((x-xc)**2)-rad**2
    if(t>0):
        pt.append(Point(x,yl))
        pt.append(Point(2*xc-x,yl))
        pt.append(Point(x,2*yc-yl))
        pt.append(Point(2*xc-x,2*yc-yl))
    else:
        pt.append(Point(x,yh))
        pt.append(Point(2*xc-x,yh))
        pt.append(Point(x,2*yc-yh))
        pt.append(Point(2*xc-x,2*yc-yh))
    
#   y=2*yc-y
#  pt.append(Point(x,y))

win=GraphWin('Circle Drawing',1000,800)

for p in pt:
    p.draw(win)

pc=Point(xc,yc)
pc.draw(win)
