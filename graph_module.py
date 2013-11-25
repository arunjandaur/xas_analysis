from __future__ import division
"""
Classes-
*Gaussian
*Histogram
"""

class Gaussian(object):
	"""
	Representation of a gaussian curve. It stores the mean and stdev of the curve.
	"""
	def __init__(self, mean, stdev):
		self.mean = mean
		self.stdev = stdev

	def get_mean(self):
		return self.mean

	def get_stdev(self):
		return self.stdev

	def __str__(self):
		return "Mean: {0}, Stdev: {1}".format(self.get_mean(), self.get_stdev())

class Histogram(object):
	"""
	Stores data points into appropriate buckets with respect to a given bucket width. i.e x = 2.6 will be stored in bucket 2 if bucket width is 1. If width is 5, then 2.6 maps to bucket 0.
	"""
	def __init__(self, name, bucket_width):
		"""
		bucket_width specifies the width of the histogram buckets. For example, if bucket_width == 10, then values 1 to 9.99 map to bucket 0. Self.buckets is a dictionary that contains bucket indices as keys and an list of _Points as values.
		"""
		self.name = name
		self.buckets = {}
		self.bucket_width = bucket_width
		self.gaussians = []


#	def add_count(self, count):
#		self.count = count
	
	def get_name(self):
		"""
		Returns the type of data this histogram holds
		"""
		return self.name

	def add_point(self, point):
		"""
		Adds a point to the histogram.
		"""
		bucket_num = int(point.get_data() / self.bucket_width)* self.bucket_width
		if bucket_num not in self.get_buckets():
			self.buckets[bucket_num] = [point]
		else:
			self.buckets[bucket_num].append(point)
	
	def get_frequency(self, bucket):
		"""
		Returns the amount in a given bucket
		"""
#		return len(self.buckets[bucket])/self.count
		return len(self.buckets[bucket])

	def get_relationships_from_bucket(self, bucket):
		"""
		Returns the relationships in a given bucket
		"""
		return self.buckets[bucket]
	
	def get_buckets(self):
		"""
		Returns the values of all the buckets
		"""
		lst = self.buckets.keys()
		lst.sort()
		return lst

	def _calculate_gaussians(self):
		"""
		Internal use only. This analyzes the different peaks in the histograms and separates them into gaussians. Used by get_gaussians
		"""
		#Gaussian detection algorithm

	def get_gaussians(self):
		"""
		Call this method when finished with adding data points. It checks if gaussians have already been found. If not, it calls _calculate_gaussians(). Then it returns a list of gaussians.
		"""
		if self.gaussians == []:
			_calculate_gaussians(self)
		return self.gaussians

	def get_gaussian(self, value, num_stdevs):
		"""
		Retrieve the gaussian curve that value belongs to. If it doesn't belong to any, this method returns None. If self.gaussians is empty, then it calls _calculate_gaussians().
		"""
		if self.gaussians == []:
			_calculate_gaussians(self)
		for gaussian in self.gaussians:
			mean = gaussian.get_mean()
			stdev = gaussian.get_stdev()
			if value <= (mean + num_stdevs * stdev) and value >= (mean - num_stdevs * stdev):
				return gaussian
		return None

	def __str__(self):
		result = ""
		for bucket in self.get_buckets():
			result += "{0} {1}\n".format(bucket, self.get_frequency(bucket))
		return result

	def str2(self):
		"""
		Returns a string representation of the histogram. Currently, it just prints the gaussians.
		"""
		result = ""
		if self.gaussians == []:
			_calculate_gaussians(self)
		for gaussian in self.gaussians:
			result += str(gaussian) + "\n"
		return result
