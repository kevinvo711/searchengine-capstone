"""
dependencies:
scikit-learn
pandas
beautifulsoup4
lxml
"""

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import scipy.sparse
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import os

def main():
    directoryName = "./data/wikipedia-trimmed" #test directory folder
    vectorizer = TfidfVectorizer(max_df=.65, min_df=1, stop_words="english", use_idf=True, norm=None) #vectorize object

    with os.scandir(directoryName) as allFiles: #opens directory folder & looks at each file
        for allDocs in allFiles:
            transDocs = vectorizer.fit_transform(allDocs)#converts the list of strings to a sparse matrix
            transDocs_as_array = transDocs.toarray() #making sure the file list has the same number of documents in the array

            len(transDocs_as_array)



"""
Uses BeautifulSoup package to parse HTML, using 'lxml' parser


@param fileName
location of file as string

@returns data in HTML page as list
"""

def parseHTML(fileName):
    with open(fileName, 'r', errors="ignore") as fn:
        soupObject = BeautifulSoup(fn, features='lxml')
        return [soupObject.get_text()]

if __name__ == "__main__":
    main()
