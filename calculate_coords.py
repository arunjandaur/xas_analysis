from __future__ import division
from math import sqrt, acos, atan2, sin
from coordinate import *
from numpy.linalg import *

def subtract(a, b):
	"""
	Input: Two points represented as Coordinates
	Output: Difference between two Atoms as a Coordinate
	"""
	x = a.get_x() - b.get_x()
	y = a.get_y() - b.get_y()
	z = a.get_z() - b.get_z()
	return Coordinate(x, y, z)

def dot_product(a, b):
	"""
	Input: Two vectors represented as Coordinates
	Output: Dot product of two vectors as a float
	"""
	a = matrix([a.get_x(), a.get_y(), a.get_z()])
	b = matrix([b.get_x(), b.get_y(), b.get_z()])
	return dot(a, b)

def cross_product(a, b):
	"""
	Input: Two vectors represented as Coordinates
	Output: Cross product of two vectors as a Coordinate
	"""
	a = matrix([a.get_x(), a.get_y(), a.get_z()])
	b = matrix([b.get_x(), b.get_y(), b.get_z()])
	cp = cross(a, b)
	x = cp[0]
	y = cp[1]
	z = cp[2]
	return Coordinate(x, y, z)

def magnitude(a):
	"""
	Input: One vector represented as a Coordinate
	Output: Magnitude of a vector as a float
	"""
	return norm([a.get_x(), a.get_y(), a.get_z()])

def distance(a, b):
	"""
	Input: Two Atoms
	Output: Distance between two Atoms as a float
	"""
	return sqrt((a.get_x() - b.get_x()) ** 2 + (a.get_y() - b.get_y()) ** 2 + (a.get_z() - b.get_z()) ** 2)

def angle(center, a, b):
	"""
	Input: Three Atoms: A central one and the two it is connected to
	Output: The central Atom's angle as a float
	"""
	a_vector = subtract(a, center)
	b_vector = subtract(b, center)
	a_dot_b = dot_product(a_vector, b_vector)
	a_vector_mag = magnitude(a_vector)
	b_vector_mag = magnitude(b_vector)
	return acos(a_dot_b / (a_vector_mag * b_vector_mag))

def dihedral(a, b, c, d):
	"""
	Input: Four Atoms
	Output: The dihedral angle among them as a float
	"""
	#IMPORTANT: THIS METHOD DOES NOT WORK!!!
	b1 = subtract(b, a)
	b2 = subtract(c, b)
	b3 = subtract(d, c)
	return atan2(cross_product_mag(b1, b2), dot_product(b2, b3))

if __name__ == "main":
	print "Distance: " + str(distance(a, b))
	print "Angle: " + str(angle(a, b, c))
	print "Dihedral: " + str(dihedral(a, b, c, d))
