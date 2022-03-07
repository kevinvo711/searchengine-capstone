"""
dependencies:
scikit-learn
pandas
beautifulsoup4
lxml
"""

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import pandas as pd
from bs4 import BeautifulSoup
import os


"""
Uses BeautifulSoup package to parse HTML, using 'lxml' parser


@param myFile
location of file as string

@returns "string" as data in HTML page
"""
def parseHTML(myFile):
    with open(myFile, 'r') as fp:
        soup = BeautifulSoup(fp, features='lxml') 
        # print(fp.read())
        # fp.seek(0)
        return soup.get_text()

def main():
    directoryName = "./data/wikipedia-trimmed"
    list = os.listdir(directoryName)
    

main()