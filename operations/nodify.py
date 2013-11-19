#Module used to create the atom node object for the nodal graph from a given xyz. Does not calculate relationships or does any sort of analysis. This simply creates the nodes to be used for that

from Nodal_Graph_Types import Nodal_Graph, Node

def atom_nodes_init(xyzFile):
	"""
	Returns a Nodal_Graph object that has all the atoms from the xyz file 
	initialized into node objects.
	"""

	xyz_file = open(xyzFile)

	graph = Nodal_Graph()


	#These two do nothing for now. Only used to increment through file.
	num_of_atoms = int(xyz_file.next())
	molecule_name = xyz_file.next()
	
	snap_num = 0
	for line in xyz_file:
		node = _create_node(line, snap_num)
		graph.add_node(node)
	
	return graph

def _create_node(xyzLine, snap_num):
	"""
	Given a string that is a line from the xyz and a snapshot number, creates a node object
	Given string must be in from of 
	[Atom] [X cord] [Y cord] [Z cord]
	"""
	split_line = xyzLine.split()
	atom_name = split_line[0]
	x_cord = float(split_line[1])
	y_cord = float(split_line[2])
	z_cord = float(split_line[3])
	return Node(atom_name, x_cord, y_cord, z_cord, snap_num)

#For testing purposes
if __name__ == "__main__":
	graph = atom_nodes_init("phenakite_ex.xyz")
