from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
import math
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

class _Bin(object):
	def __init__(self, left, right):
		self.left = left
		self.right = right
		self.points = []
		self.x = (left + right) / 2
		self.frequency = 0

	def add_point(self, point):
		self.points.append(point)
		self.frequency += 1
		total_x = 0
		for point in self.points:
			total_x += point.get_data()
		self.x = total_x / self.frequency
		self.expand()

	def expand(self):
		pass

	def get_x(self):
		return self.x

	def get_frequency(self):
		return self.frequency

	def __str__(self):
		return "{0} {1}".format(self.x, self.get_frequency())

class Histogram(object):
	"""
	Stores data points into appropriate buckets with respect to a given bucket width. i.e x = 2.6 will be stored in bucket 2 if bucket width is 1. If width is 5, then 2.6 maps to bucket 0.
	"""
	def __init__(self, name, bin_width, filter_size):
		"""
		bucket_width specifies the width of the histogram buckets. For example, if bucket_width == 10, then values 1 to 9.99 map to bucket 0. Self.buckets is a dictionary that contains bucket indices as keys and an list of _Points as values.
		"""
		self.name = name
		self.bins = []
		self.bin_width = bin_width
		self.filter_size = filter_size
		self._init_bins()
		self.gaussians = []
		self.count = 0

	def _init_bins(self):
		num_bins = int(math.ceil(self.filter_size / self.bin_width))
		for i in range(num_bins):
			left = i * self.bin_width
			right = (i+1) * self.bin_width
			self.bins.append(_Bin(left, right))

	def get_name(self):
		"""
		Returns the type of data this histogram holds
		"""
		return self.name

	def add_point(self, point):
		"""
		Adds a point to the histogram.
		"""
		bin_num = int(point.get_data() / self.bin_width)
		self.bins[bin_num].add_point(point)
		self.count += 1

	def spline(self):
		x = []
		y = []
		for bin_ in self.bins:
			x.append(bin_.get_x())
			y.append(bin_.get_frequency())
		x = np.array(x)
		y = np.array(y)
		tck = interpolate.splrep(x, y, s=0)
		x_new = np.arange(x[0], x[-1], .001)
		y_new = interpolate.splev(x_new, tck, der=0)
		return (x_new, y_new)

	def draw_spline(self, x, y):
		plt.figure()
		plt.plot(x, y)
		plt.show()

	def _calculate_gaussians(self):
		"""
		Internal use only. This analyzes the different peaks in the histograms and separates them into gaussians. Used by get_gaussians
		"""
		#Gaussian detection algorithm
		pass

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
		for bin_ in self.bins:
			result += str(bin_)  + "\n"
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
