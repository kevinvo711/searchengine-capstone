import json
from flask import Flask, render_template, request, redirect
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sys
import csv
import pickle

csv.field_size_limit(sys.maxsize)

app = Flask(__name__)
tfIdfVectorizer = TfidfVectorizer()
df = pd.read_pickle('data.pkl', compression='infer')
tfIdf = tfIdfVectorizer.fit_transform(df['text'])

@app.route('/test', methods=['POST', 'GET'])
def test():
    if request.method == "POST":
        searchquery = request.form['text']   # vectorize search term
        if (searchquery != ""):
            q_vec = tfIdfVectorizer.transform([searchquery])
            results = cosine_similarity(tfIdf,q_vec).reshape((-1,))
            results_list = []
            newresults = results.argsort()[-51:][::-1]
            for i in newresults:
                results_list.append({'id': str(df.iloc[i,0]),
                                    'title': str(df.iloc[i,1]),
                                    'url': str(df.iloc[i,2]),
                                    'description': str(df.iloc[i,3])})
                with open("../client/src/results.json", "w", encoding ='utf8') as write_file:
                    json.dump(results_list, write_file)
            return redirect('/')
        return redirect('/')

if __name__ == "__app__":
    app.run(port=8000, debug=True)
