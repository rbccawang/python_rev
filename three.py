# script: file intended to be ran directly and contains statements outside the scope of any class or function
# module: files meant to be imported into other modules or scripts. defines classes, variables, and functions
# package: collection of related modules (dateutil, email, json)
# Python Standard Library
 
# use python's math library

import math

x1 = 0.0
y1 = 0.0
x2 = 3.0
y2 = 4.0

# calculate the euclidian distance / distance between (x1,y1) and (x2,y2)
distance = math.dist((x1,y1), (x2,y2))

print ("distance between the two points: ", distance)
