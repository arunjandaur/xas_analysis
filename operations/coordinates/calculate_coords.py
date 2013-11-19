from __future__ import division
from math import sqrt, acos, atan2, sin
from Atom import *

#Vectors are lists
#1st element = X coordinate
#2st element = Y coordinate
#3t element = Z coordinate

def distance(a, b):
	return sqrt((a.get_x() - b.get_x()) ** 2 + (a.get_y() - b.get_y()) ** 2 + (a.get_z() - b.get_z()) ** 2)

def subtract(a, b):
	x = a.get_x() - b.get_x()
	y = a.get_y() - b.get_y()
	z = a.get_z() - b.get_z()
	return Atom(a.get_name(), x, y, z)

def dot_product(a, b):
	return a.get_x() * b.get_x() + a.get_y() * b.get_y() + a.get_z() * b.get_z()

def cross_product_mag(a, b):
	return magnitude(a) * magnitude(b) * sin(angle(Atom("0", 0, 0, 0), a, b))

def magnitude(a):
	return sqrt(a.get_x() ** 2 + a.get_y() ** 2 + a.get_z() ** 2)

def angle(center, a, b):
	#Returns angle in radians
	return acos(dot_product(subtract(a, center), subtract(b, center)) / (magnitude(subtract(a, center)) * magnitude(subtract(b, center))))

def dihedral(a, b, c, d):
	b1 = subtract(b, a)
	b2 = subtract(c, b)
	b3 = subtract(d, c)
	return atan2(cross_product_mag(b1, b2), dot_product(b2, b3))

def test(a, b, c, d):
	print "Distance: " + str(distance(a, b))
	print "Angle: " + str(angle(a, b, c))
	print "Dihedral: " + str(dihedral(a, b, c, d))
