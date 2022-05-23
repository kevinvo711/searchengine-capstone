#Manual implementation of TF-IDF to mimic the libary that's in Sklearn
from scipy.sparse import csr_matrix
from sklearn.preprocessing import normalize
import numpy as np
from collections import Counter
import math

"""
IMPORTANT
USAGE:
from termfreq import TFIDF

tfidf = TFIDF(<your corpus of text here>).getOutput() 
#returns a sparse matrix of TFIDF values, similar to sklearn library
"""

class TFIDF:
    def __init__(self, corpus):
        self.sparsematrix = csr_matrix

        def IDF(corpus, unique_words):
            idf_dict = {}
            N = len(corpus)
            for i in unique_words:
                count=0
                for sentence in corpus:
                    if i in sentence.split():
                        count += 1
                    idf_dict[i] = (math.log((1+N)/(count+1)))+1 #Add 1 to avoid divide by 0 error
            return idf_dict 

        def fit(whole_data):
            unique_words = set()
            if isinstance(whole_data, (list,)):
                for x in whole_data:
                    for y in x.split():
                        #commented out because of importance of numbers in our use case
                        # if len(y)<2: #ignore words with length of less than 2
                        #     continue
                        unique_words.add(y)
                unique_words = sorted(list(unique_words))
                vocab = {j:i for i,j in enumerate(unique_words)}
            Idf_values_of_all_unique_words = IDF(whole_data,unique_words)

            return vocab, Idf_values_of_all_unique_words 
        
        def transform(dataset,vocabulary,idf_values):
            self.sparse_matrix = csr_matrix( (len(dataset), len(vocabulary)), dtype=np.float64)
            for row in range(0,len(dataset)):
                number_of_words_in_sentence=Counter(dataset[row].split())
                for word in dataset[row].split():
                    if word in list(vocabulary.keys()):
                        tf_idf_value = (number_of_words_in_sentence[word]/len(dataset[row].split()))*(idf_values[word])
                        self.sparse_matrix[row,vocabulary[word]] = tf_idf_value
            # print("NORM FORM\n",normalize(self.sparse_matrix, norm='l2', axis=1, copy=True, return_norm=False))
            output = normalize(self.sparse_matrix, norm='l2', axis=1, copy=True, return_norm=False)
            return output

            
        Vocabulary, idf_of_vocabulary = fit(corpus) 
        final_output = transform(corpus, Vocabulary, idf_of_vocabulary)
        self.sparsematrix = final_output
        # print(final_output.shape, "FINAL OUTPUT")

    def getOutput(self):
        return self.sparsematrix