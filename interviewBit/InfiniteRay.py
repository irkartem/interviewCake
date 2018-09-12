#!/usr/bin/env python3
# Author: artemirk@gmail.com

points = [(0, 0), (1, 1), (1, 2)]
points = [(6, 7), (1, 1), (33, 33)]

x = points[0][0]
y = points[0][1]

steps = 0
for pp in points:
   if  (x,y) == pp:
       continue
   dx = abs(pp[0]-x)
   dy = abs(pp[1]-y)
   ind = max(dy,dx)-min(dy,dx)
   shrd = max(dy,dx)-ind
   print("From {} to {} in {} diagonal steps and {} direct".format([x,y],pp,shrd,ind))
   steps += ind+shrd
   x = pp[0]
   y = pp[1]

print(steps)
