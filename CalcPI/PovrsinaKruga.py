#! /usr/local/bin/python3.6
# površina kruga r = 5

#import math
from math import *

r = 5

Pkr = r * r * pi
print(Pkr)

n = 100000000 # number of sides polygon inside circle

def area_of_polygon_inside_circle(circle_radius, number_of_sides):
    return round(0.5 * n * r ** 2 * sin(2 * pi / n), 40)

Pp = area_of_polygon_inside_circle(r, n)
print(Pp)