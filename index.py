import pandas as pd
import numpy as np
import os
import termlist

"Implementing the index for the search engine"

def process_files(directoryName): #reading from the wikipedia directory
	file_to_terms = {}
	for file in directoryName:
		pattern = re.compile('[\W_]+')
		file_to_terms[file] = open(file, 'r').read().lower(); #open file to read them
		file_to_terms[file] = pattern.sub(' ',file_to_terms[file])
		re.sub(r'[\W_]+','', file_to_terms[file])
		file_to_terms[file] = file_to_terms[file].split()
	return file_to_terms

def index_one_file(termlist):
	fileIndex = {}
	for index, word in enumerate(termlist):
		if word in fileIndex.keys():
			fileIndex[word].append(index)
		else:
			fileIndex[word] = [index]
	return fileIndex

    def make_indices(termlists):
	total = {}
	for directoryName in termlists.keys():
		total[directoryName] = index_one_file(termlists[directoryName])
	return total

def fullIndex(regdex):
	total_index = {}
	for directoryName in regdex.keys():
		for word in regdex[directoryName].keys():
			if word in total_index.keys():
				if directoryName in total_index[word].keys():
					total_index[word][directoryName].extend(regdex[directoryName][word][:])
				else:
					total_index[word][directoryName] = regdex[directoryName][word]
			else:
				total_index[word] = {directoryName: regdex[directoryName][word]}
	return total_index
