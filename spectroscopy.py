class Spectroscopy(object):
	"""
	Data type to store the spectroscopy values for each snapshot

	///Important///
	Has yet to be fully flushed out so is not fully compatible with the 
	nodal graph.  
	Ideas:
	1)Have the nodal graph store each spectroscopy related to their snapshot number 
	through a dictionary
	2)Reformat the Node in the graph to be more generalized so that atoms, probability graphs,
	and spectroscopies can be stored in individual nodes. For this a base node class will simply hold all the connections 
	it has. All inherited versions such as atoms and probablity graphs will have unique identifiers and data for each node
	but can still be treated like a node
	In addition, connections can also be more generalized so that 
	the base class just stores who it is connected to while a child class of relationship stores meaningful data 
	when the connection between two nodes has to store that
	"""
	def __init__(self, filename):
		"""
		Takes in the filename of a spectra file and then parses it, storing energies as keys and corresponding intensities as values.
		"""
		self.intensities = {}
		spec_file = open(filename, 'r')
		self.min_energy = float('inf')
		self.max_energy = 0
		for line in spec_file.readlines():
			if '#' in line:
				continue
			else:
				line = line.split()
				energy = float(line[0])
				intensity = float(line[1])
				if energy < self.min_energy:
					self.min_energy = energy
				if energy > self.max_energy:
					self.max_energy = energy
				self.intensities[energy] = intensity

	def get_min_energy(self):
		"""Returns the smallest energy values"""
		return self.min_energy

	def get_max_energy(self):
		"""Returns the largest energy values"""
		return self._max_energy

	def get_intensity(self, energy):
		"""
		Return the intensity level corresponding to a certain energy, if it exists. NOTE: maybe we should return the intensity of the energy level closest to the paramter.
		"""
		if energy not in self.intensities.keys():
			print "404. Energy level not found."
		else:
			return self.intensities[energy]

	def get_intensities(self, energy_min=0, energy_max=float('inf')):
		"""
		Return a list of intensities that correspond to an energy range specified by energy_min and energy_max. 0 and infinity are the defaults, which will return all the intensities.
		"""
		if energy_min == 0 and energy_max == float('inf'):
			return self.intensities.values()
		result = []
		for energy in self.intensities.keys():
			if energy >= energy_min and energy <= energy_max:
				result.append(self.get_intensity(energy))
		return result

	def __str__(self):
		result = ""
		for energy in self.intensities:
			result += "E: {0}, I: {1}\n".format(energy, self.intensities[energy])
		return result
