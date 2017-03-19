import os

class Dirswalk(object):
	"""API for getting directory walking collections"""

	def __init__(self,path):
		self.path = path

	@property
	def path(self):
		return self._path

	@path.setter
	def path(self, value):

		if	os.path.exists(value):
			self._path = value
		else:
			raise Exception("{} is not a valid path".format(value))
			

	def walkpaths(self):
		"""Return the path to all the files in a directory recursively"""

		path_collection = []

		for dirpath, dirnames, filenames in os.walk(self.path):
			for file in filenames:
				full_path = os.path.join(dirpath,file)
				path_collection.append(full_path)

		return path_collection


	def walkfiles(self):
		"""Return all files in a directory"""

		file_collection = []
		for dirpath, dirnames, filenames in os.walk(self.path):
			for file in filenames:
				file_collection.append(file)

		return file_collection


	def walkdirs(self):
		"""Return all files in a directory"""

		dir_collection = []
		for dirpath, dirnames, filenames in os.walk(self.path):
			for dirname in dirnames:
				dir_collection.append(dirname)

		return dir_collection


if __name__ == '__main__':
	dw  = Dirswalk('/tmp')
	print ("\nRecursive listing of all paths in a dir:")
	for path in dw.walkpaths():
		print(path)
	print ("\nRecursive listing of all files in dir:") 
	for file in dw.walkfiles():
		print(file)
	print ("\nRecursive listing of all dirs in dir:")
	for dir in dw.walkdirs():
		print(dir)