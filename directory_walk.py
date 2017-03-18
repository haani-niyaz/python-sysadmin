'''
Directory walking script
'''

import os
path = '/tmp'

def walkpaths(path=path):
	"""Return the path to all the files in a directory recursively"""

	path_collection = []

	for dirpath, dirnames, filenames in os.walk(path):
		for file in filenames:
			full_path = os.path.join(dirpath,file)
			path_collection.append(full_path)

	return path_collection


def walkfiles(path=path):
	"""Return all files in a directory"""

	file_collection = []
	for dirpath, dirnames, filenames in os.walk(path):
		for file in filenames:
			file_collection.append(file)

	return file_collection


def walkdirs(path=path):
	"""Return all files in a directory"""

	dir_collection = []
	for dirpath, dirnames, filenames in os.walk(path):
		for dirname in dirnames:
			dir_collection.append(dirname)

	return dir_collection


if __name__ == '__main__':

	print ("\nRecursive listing of all paths in a dir:")
	for path in walkpaths():
		print(path)
	print ("\nRecursive listing of all files in dir:") 
	for file in walkfiles():
		print(file)
	print ("\nRecursive listing of all dirs in dir:")
	for dir in walkdirs():
		print(dir)