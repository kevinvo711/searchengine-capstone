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


"""
Dirty implementation of a set of test HTML files for running TF-IDF on.
Ideally can run on any HTML page, and produce a {key:value} dictionary of every 'word' with 'tf-idf' value
Ran on a test set of 50 files successfully

"""

def main():
    directoryName = "./data/wikipedia-trimmed"
    # testDirectory = "./testfolder"
    vectorizer = TfidfVectorizer(stop_words="english") #vectorizer object of TfidfVectorizer class

    myDictionaryTuple = {}
    dictionaryList = []
    with os.scandir(directoryName) as allMyFiles: #opens the directory folder and iterates through every file (expected input is html page)
        for eachFile in allMyFiles:
            matrixObj = vectorizer.fit_transform(parseHTML(eachFile)) #vectorizer needs to transform on a dictionary/list - type object
            tokens = vectorizer.get_feature_names_out() #the list of words'

            """
            # myDictionaryTuple = dict(zip(tokenList, [matrixObj.toarray()))
            # myDictionaryTuple = {key:value for key, value in zip(tokens,matrixObj.toarray())}
            """

            cooMatrix = matrixObj.tocoo() #convert scipy.sparse matrix to coordinate format matrix, to able iterate through the data values
           
            """
            # for i, j, v in zip(cooMatrix.row, cooMatrix.col, cooMatrix.data):
            #     print ("(%d, %d), %s" % (i, j, v))
            # cooMatrix = scipy.sparse.coo_matrix(matrixObj)
            """
            myDictionaryTuple = dict(zip(tokens,cooMatrix.data))
            dictionaryList.append(myDictionaryTuple)

    """Have dictionary of stuffs, now to put it into Postgresql"""

    myDf = pd.DataFrame(data=matrixObj.toarray(), columns=tokens) #just for formatting and to look inside

    print(myDictionaryTuple)
    print(myDf.head(30))
    transposed = myDf.transpose()  # 2
    print(transposed.head(30))  # 1
    # transposed = transposed.sort_index(axis=1, ascending=False) 
    print(transposed.head(30))
    print(len(dictionaryList)) #run on list of html pages, should equal to number of files in directory, in this case, 50




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

