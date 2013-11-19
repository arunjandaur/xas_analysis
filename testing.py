from Spectroscopy import Spectroscopy#For Testing 
from Init_Relationships import relationships_init
from Nodify import atom_nodes_init #For Testing
from Analyzer import Analyzer#For Testing
import sys #For Testing
import os #For Testing
import re #For Testing


xyz_file = sys.argv[1]
spectra_folder = sys.argv[2]	

#Init the nodes and relationships, like distances, dihedrals, etc.
graph = atom_nodes_init(xyz_file)
relationships_init(graph)

#Add the spectra to the graph
spectra_files = os.listdir(spectra_folder)
for spectrum in spectra_files:
	#spec_num = re.sub(r'(.*?)-.*', r'\1', spectrum)
	spec_num = int(re.sub(r'.*?([0-9]*)-.*', r'\1', spectrum))
	spec = Spectroscopy(spectra_folder + "/" + spectrum)
	graph.add_spectrum(spec_num, spec)
	
#Create the histogram
analyzer = Analyzer(graph)
histogram = analyzer.create_distance_probability("Distance S - S", .5, 0, 10)
#print graph
print histogram

