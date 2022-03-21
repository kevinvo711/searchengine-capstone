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
    directoryName = "./data/wikipedia-trimmed"
    testDirectory = "./testfolder"
    vectorizer = TfidfVectorizer(stop_words="english") #vectorizer object of TfidfVectorizer class
    # X = vectorizer.fit_transform()

    simple = []
    for i in range(424):
        simple.append(i)

    myDictionaryTuple = {}
    dictionaryList = []
    with os.scandir(directoryName) as allMyFiles:
        for eachFile in allMyFiles:
            matrixObj = vectorizer.fit_transform(parseHTML(eachFile)) #vectorizer needs to transform on a dictionary/list - type object
            tokens = vectorizer.get_feature_names_out()
            tokenList = []
            # myDictionaryTuple = dict(zip(tokenList, [matrixObj.toarray()))
            # myDictionaryTuple = {key:value for key, value in zip(tokens,matrixObj.toarray())}
            cooMatrix = matrixObj.tocoo()
            # for i, j, v in zip(cooMatrix.row, cooMatrix.col, cooMatrix.data):
            #     print ("(%d, %d), %s" % (i, j, v))
            # cooMatrix = scipy.sparse.coo_matrix(matrixObj)
            myDictionaryTuple = dict(zip(tokens,cooMatrix.data))
            dictionaryList.append(myDictionaryTuple)


    myDf = pd.DataFrame(data=matrixObj.toarray(), columns=tokens)

 
    # print(len(myDictionaryTuple))
    # print(myDictionaryTuple)
    # print(matrixObj)
    # print(myDf.head(30))
    # transposed = myDf.transpose()
    # print(transposed.head(30))
    # transposed = transposed.sort_index(axis = 1, ascending = False)
    # print(transposed.head(30))
    print(len(dictionaryList))


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

