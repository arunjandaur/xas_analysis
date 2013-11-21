from numpy.linalg import *
from numpy import *
from math import sin, cos

def lattice_xyz_matrix(alpha, beta, gamma):
	"""
	Returns a transformation matrix that will yield cartesian coordinates when lattice coordinates are RIGHT multiplied by this transformation matrix.
	Coordinates are row vectors. i.e: [a b c]
	"""
	matrx = []
	matrx.append([1, 0, 0])
	matrx.append([cos(alpha), sin(alpha), 0])
	matrx.append([cos(alpha)*cos(beta), cos(alpha)*sin(beta), sin(beta)])
	return matrix(matrx)

def xyz_lattice_matrix(alpha, beta, gamma):
	"""
	Returns a transformation matrix that will yield lattice coordinates when cartesian coordinates are RIGHT multiplied by this transformation matrix.
	Coordinates are row vectors. i.e: [x y z]
	"""
	return inv(lattice_xyz_matrix(alpha, beta, gamma))

def lattice_to_xyz(lattice_vectors, alpha, beta, gamma):
	"""
	Input:
		lattice_vectors (numpy matrix): A collection of row vectors in lattice coordinates
		alpha (float), beta (float), and gamma (float): The lattice angles as floats
	Output:
		A collection of row vectors in xyz coordinates as a numpy array
	"""
	return inner(lattice_vectors, lattice_xyz_matrix(alpha, beta, gamma)) #Inner product of lattice row vectors and lattice to XYZ transformation matrix


def xyz_to_lattice(cartesian_vectors, alpha, beta, gamma):
	"""
	Vice versa of lattice_to_xyz
	"""
	return inner(cartesian_vectors, xyz_lattice_matrix(alpha, beta, gamma)) #Inner product of cartesian row vectors and XYZ to lattice transformation matrix
