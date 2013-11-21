import random
from coordinate import *
from spectroscopy import Spectroscopy

class NodalGraph(object):
	"""
	Main data type for storing all the nodes of an inputs file
	/Nodes are stored within a doubled keyed dictionary with lists
	The first index is the snapshot number
	The second index is the name of the atom
	The final part is a list that stores all the nodes that represent 
	atoms from the same snapshot and same atom type/

	/Connections are stored within a doubled keyed dictionary with lists
	The first key is a snapshot number
	The second key is the relationship type
	The final part is a list that stores all the connections that represent 
	connections from the same snapshot with the same relationship type/

	Since not every snapshot will have the same amount of relationships due to how we filter,
	I think it best to store all the possible relationships in all the snapshots in a 
	list.

	IMPORTANT abstraction note: Any method that takes in atom's name or snapshot name/number as a parameter should be called by getting the atom names or the snapshots using the getter methods and then looping through the results and passing those into the desired method. DO NOT make ANY assumptions about what the atoms are called or how the snapshot names or numbers are stored. 
	"""
	def __init__(self):
		self.nodes  = {}
		self.connections = {}
		self.relationships = []
		self.spectra = {}

	def add_node(self, node):
		"""Adds a node"""
		assert isinstance(node, Node)
		snap_num = node.get_snap_num()
		name = node.get_name()
		if not self.nodes.has_key(snap_num):
			self.nodes[snap_num] = {}
		if not self.nodes[snap_num].has_key(name):
			self.nodes[snap_num][name] = []

		self.nodes[snap_num][name].append(node)

	def get_atom_type(self, snap_num, name):
		"""Returns a list of all the nodes that have the same name and 
		are from the same snapshot"""
		return self.nodes[snap_num][name]

	def get_snapshots(self):
		"""Returns a list of all the snapshots stored in the graph"""
		return self.nodes.keys()

	def get_names(self):
		"""Returns a list of all the atom types in the graph
		Since all the snapshots have the same atom_types, this will return 
		a list of names from an arbitrary snapshot"""
		return random.choice(list(self.nodes.values())).keys()	
	
	def add_connection(self, connection):
		"""Adds a connection"""
		assert isinstance(connection, Connection)
		snap_num = connection.get_snap_num()
		relationship = connection.get_relationship()
		if not self.connections.has_key(snap_num):
			self.connections[snap_num] = {}
		if not self.connections[snap_num].has_key(relationship):
			self.connections[snap_num][relationship] = []
			if not relationship in self.relationships:
				self.relationships.append(relationship)		
		
		self.connections[snap_num][relationship].append(connection)
	
	def get_relationships(self):
		"""Returns a list of all the types of relationships in the graph"""
		return self.relationships	
		
	def get_connections(self, snap_num, relationship):
		"""Returns a list of all the connections grouped by the snapshot and
		relationship given
		///////This needs to be refined because not every snapshot will have the 
		same relationships in them based on how we filter/////////////"""
		return self.connections[snap_num][relationship]

	def add_spectrum(self, index, spectroscopy):
		assert isinstance(spectroscopy, Spectroscopy)
		self.spectra[index] = spectroscopy

	def get_spectrum(self, index):
		return self.spectra[index]

	def __str__(self):
		answer = ""
		for snap_num in self.nodes:
			for name in self.nodes[snap_num]:
				for atom in self.nodes[snap_num][name]:
					answer += "---{0}---\n".format(atom.get_name())
					for relationship in atom.get_relationships():
						for connection in atom.get_connections(relationship):
							answer += "  " + str(connection) + "\n"

		answer += "\n\n"
		
		for spec_num in self.spectra:
			answer += "#{0}:\n{1}\n".format(spec_num, self.spectra[spec_num])

		return answer

class Atom(object):
	def __init__(self, name, x, y, z):
		self.name = name
		self._coordinate = Coordinate(x, y, z)

	def get_name(self):
		"""Returns a string of the name of the atom type"""
		return self.name

	def get_x(self):
		"""Returns a float of the x coordinate"""
		return self._coordinate.get_x()

	def get_y(self):
		"""Returns a float of the y coordinate"""
		return self._coordinate.get_y()

	def get_z(self):
		"""Returns a float of the z coordinate"""
		return self._coordinate.get_z()

class Node(Atom):
	"""Node will represent an atom.
	It will contain information about the atom's
	*xyz coordinate 
	*snapshot number from which it originated
	*meaningful connections it has with other nodes
	Connections are stored within a dictionary of lists
	The dictionary keys will be the relationships of a connection
	e.x. distance between C-C
	The lists within the dictionary will store each connection, grouped by 
	the same relationship
	"""
	def __init__(self, name, x, y, z, snap_num, spectra=None):
		super(Node, self).__init__(name, x, y, z)
		self.snap_num = snap_num
		self.connections = {}
		self.spectra = spectra

	def get_snap_num(self):
		"""Returns a float of the snapshot_number"""
	 	return self.snap_num

	def get_spectra(self):
		"""Returns a spectroscopy class that stores the spectra for this atom"""
		return spectra

	def add_connection(self, connection):
		"""Adds a new connection to the dictionary of connections"""
		if self.connections.has_key(connection.get_relationship()):
			self.connections[connection.get_relationship()].append(connection)
		else:
			self.connections[connection.get_relationship()] = [connection]
	
	def remove_connection(self,connection):
		"""Removes a connection"""
		self.connections[connection.get_relationship()].remove(connection)

	def get_relationships(self):
		"""Returns a list of all the relationships connected to this node"""
		return self.connections.keys()

	def get_connections(self, relationship):
		"""Returns a list of connections grouped by their relationship"""
		return self.connections[relationship]

class Connection(object):
	"""
	Connection will represent a relationship between two or more atoms.
	This can be any relationship that has a numerical value associated with it 
	such as distances and angles.
	Connection stores all the atoms that contribute to this relationship, the 
	snapshot from which it originated, the name of the relatioship, and the 
	actual data that describes the relationship
	"""
	def __init__(self, snap_num, relationship, data):
		self.snap_num = snap_num
		self.neighbors = []
		self.relationship = relationship
		self.data = data

	def get_neighbors(self):
		"""Returns a list of all the neighbors"""
		return self.neighbors

	def get_relationship(self):
		"""Returns a string that tells the type of relationship this connections holds
		between the neighbors"""
		return self.relationship

	def get_data(self):
		"""Returns a numerical data value(possibly float) of the relationship"""
		return self.data
	
	def get_snap_num(self):
		"""Returns an int of a snapshot number"""
		return self.snap_num

	def add_neighbor(self, neighbor):
		"""Adds a neighbor to the connection"""
