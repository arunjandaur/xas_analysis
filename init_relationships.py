#Module used to create relationship objects for a given nodal_graph with only atom nodes.
from calculate_coords import distance, angle, dihedral
from nodify import atom_nodes_init #For Testing
from nodal_graph import Link
from graph_module import Histogram
import sys

FILTER_SIZE = 3

def relationships_init(node_graph):
	"""
	Given a nodal graph with only atom nodes, constructs the relationship between the nodes within 
	each snapshot and adds them to the given graph
	Does not return anything because node_graph is a reference and can be altered in place
	
	Func_parameters can be found on the very bottom

	Within this module, this is the only function that should be called from other programs. 
	Everything else is a helper function
	"""
	filter_size = 6
	bucket_width = .05

	for func in func_parameters:
		func(node_graph, filter_size)

	relationships = node_graph.get_relationships()
	histograms = []
	for relationship in relationships:
		histogram = _create_prob_graphs(node_graph, relationship, bucket_width)
		histograms.append(histogram)
	
	for histogram in histograms:
		fil = open(histogram.get_name(), 'w')
		fil.write(str(histogram))
		fil.close()

#Distances
def _create_distances(node_graph, filter_size = FILTER_SIZE):
	"""
	Given a nodal graph and a maximum filter size, creates distances relationships for all
	the atoms nodes and then binds them to the nodes and the graph
	"""
	snap_nums = node_graph.get_snapshots()

	for snap in snap_nums:
		_make_distance_for_snap(snap, node_graph, filter_size)
			
def _make_distance_for_snap(snap, node_graph, filter_size = 3):
	atomic_names = node_graph.get_names()
	
	i = 0 
	while i < len(atomic_names):
		for atom_1 in node_graph.get_atom_type(snap, atomic_names[i]):
			for other_type in atomic_names[i:]:
				for atom_2 in node_graph.get_atom_type(snap, other_type):
					distance_data = distance(atom_1, atom_2)
					if distance_data <= filter_size and distance_data > 0:
						relationship = "Distance {0} - {1}".format(atom_1.get_name(), atom_2.get_name())
						dist_con = Link(snap, relationship, distance_data)
						dist_con.add_neighbor(atom_1)
						dist_con.add_neighbor(atom_2)
						atom_1.add_link(dist_con)
						atom_2.add_link(dist_con)
						node_graph.add_link(dist_con)
		i = i + 1
		
#Angles
def _create_angles(node_graph):
	pass

#Dihedrals
def _create_dihedrals(node_graph):
	pass

#Probabilities
def _create_prob_graphs(node_graph, relationship, bucket_width):
	snapshot_keys = node_graph.get_snapshots()
	histogram = Histogram(relationship, bucket_width)
	
	for snap_key in snapshot_keys:
		links = node_graph.get_links(snap_key, relationship)
		
		for link in links:
			histogram.add_point(link)
			
	return histogram

def relationship_vs_intensity(graph, relationship, energy_min, energy_max):
	"""Pretend this DOES NOT exist"""
	snapshot_keys = graph.get_snapshots()
	xy_graph = XY_Graph()
	
	for snap_key in snapshot_keys:
		links = self.graph.get_links(snap_key, relationship)
		spectrum = self.graph.get_spectrum(snap_key)
		intensities = spectrum.get_intensities(energy_min, energy_max)
		
		for link in links:
			data = link.get_data()
			for intensity in intensities:
				xy_graph.add_point(data, intensity)
				
	return xy_graph

func_parameters = [_create_distances]

#For Testing Purposes
if __name__ == "__main__":	
	xyz = sys.argv[1]
	graph = atom_nodes_init(xyz)
	relationships_init(graph)

