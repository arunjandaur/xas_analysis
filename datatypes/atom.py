class Atom(object):
	def __init__(self, name, x, y, z):
		self.name = name
		self.x = x
		self.y = y
		self.z = z

	def get_name(self):
		"""Returns a string of the name of the atom type"""
		return self.name

	def get_x(self):
		"""Returns a float of the x coordinate"""
		return self.x

	def get_y(self):
		"""Returns a float of the y coordinate"""
		return self.y

	def get_z(self):
		"""Returns a float of the z coordinate"""
		return self.z
