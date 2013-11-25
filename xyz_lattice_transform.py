from numpy.linalg import *
from numpy import *
from math import radians, sin, cos, pow

class Lattice_Transform(object):
	
	def __init__(self, a, b, c, alpha, beta, gamma):
		"""
		Initializes a transformation matrix for xyz to lattice conversion an vice_versa
		Inputs:
			a,b,c = lenghts of lattice vectors(Angstrom)
			alpha, beta, gamma = angles between lattice vectors(in degrees)
		"""
		rad_alpha = radians(alpha)
		rad_beta = radians(beta)
		rad_gamma = radians(gamma)
		self.lat_2_xyz_mat = self._lattice_xyz_matrix( a, b, c, rad_alpha, rad_beta, rad_gamma)
		self.xyz_2_lat_mat = self._xyz_lattice_matrix(a, b, c, rad_alpha, rad_beta, rad_gamma)


	def _lattice_xyz_matrix(self, a, b, c, alpha, beta, gamma):
		"""
		Inputs:
			a,b,c = lenghts of lattice vectors(Angstrom)
			alpha, beta, gamma = angles between lattice vectors(in radians)
			
		Returns a transformation matrix that will yield cartesian coordinates 
		when lattice coordinates are RIGHT multiplied by this transformation matrix.
		"""
		matrx = []
		matrx.append([a, 0, 0])
		matrx.append([b*cos(gamma),b*sin(gamma), 0])
		matrx.append([c*cos(beta), c*cos(alpha)*sin(alpha), c*sqrt(1-(pow(cos(beta),2)+pow(cos(alpha)*sin(gamma),2)))])
		return array(matrx)

	def _xyz_lattice_matrix(self, a, b, c, alpha, beta, gamma):
		"""
		Returns a transformation matrix that will yield lattice coordinates when cartesian coordinates are RIGHT multiplied by this transformation matrix.
		Coordinates are row vectors. i.e: [x y z]
		"""
		return inv(self._lattice_xyz_matrix(a, b, c, alpha, beta, gamma))

	def lattice_to_xyz(self, lattice_vectors):
		"""
		Input:
			lattice_vectors (numpy array): A collection of row vectors in lattice coordinates
		Output:
			A collection of row vectors in xyz coordinates as a numpy array
		"""
		#Inner product of lattice row vectors and lattice to XYZ transformation matrix	
		return dot(lattice_vectors, self.lat_2_xyz_mat) 


	def xyz_to_lattice(self, cartesian_vectors):
		"""
		Vice versa of lattice_to_xyz
		"""
 		#Inner product of cartesian row vectors and XYZ to lattice transformation matrix
		return dot(cartesian_vectors, self.xyz_2_lat_mat)
	
	def shift_periodicity(self, lattice_vectors, dx):
		"""
		Given a set of lattice vectors, will apply a shift to them and then adjust them for periodicity
		"""
		return lattice_vectors + dx - floor(lattice_vectors + dx)

if __name__ == "__main__":
	#Specifically test phenakite
	mat = Lattice_Transform(12.69451,12.69451,8.34858,90,90,120)
	out_put = open("lat_test_ex.xyz","w")
	with open("phenakite_ex.xyz","r") as xyz_file:
		out_put.write(xyz_file.next())
		out_put.write(xyz_file.next())
		for line in xyz_file:
			split_line = line.split()
			atom_name = split_line[0]
			x = float(split_line[1])
			y = float(split_line[2])
			z = float(split_line[3])
			xyz_array = array([x,y,z])
			lats = mat.xyz_to_lattice(xyz_array)
			new_lats = mat.shift_periodicity(lats, 0.7894565132)
			new_xyz = mat.lattice_to_xyz(new_lats)
			out_string = "{0} {1} {2}\n".format(*new_xyz)
			out_put.write(atom_name + " " + out_string)
