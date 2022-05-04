from platform import python_branch
from flask import Flask
from flask import request
import json
from flask import jsonify
# import psycopg2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
import sys
import csv

csv.field_size_limit(sys.maxsize)

app = Flask(__name__)


@app.route('/flask', methods=['GET'])
def index():
    return "Flask server"


# connect to database
# HOST = "localhost"
# USERNAME = "postgres"
# PASSWORD = "password"
# DATABASE = "starter-server"
# PORT = "5432"

# db = psycopg2.connect(host=HOST, user=USERNAME,
#                       password=PASSWORD, database=DATABASE)
# cursor = db.cursor()

@app.route('/test', methods=['POST', 'GET'])
def test():
    tfIdfVectorizer = TfidfVectorizer()
    col_names = ["id", "title", "url", "text"]
    df = pd.read_csv('data.csv', encoding='utf-8', sep='^', names=col_names, error_bad_lines=False, engine='python')
    df.head()
    tfIdf = tfIdfVectorizer.fit_transform(df['text'])
    query = request.form['text']
    # vectorize search term
    q_vec = tfIdfVectorizer.transform([query])
    results = cosine_similarity(tfIdf,q_vec).reshape((-1,))
    for i in results.argsort()[-10:][::-1]:
        print(df.iloc[i,0],"--",df.iloc[i,1])
    return "Searching for " + query


    # # calculate cossim
    # sim = {}

    # for i in range(10):
    #     sim[i] = np.dot(df.loc[:, i].values, q_vec) / np.linalg.norm(df.loc[:, i]) * np.linalg.norm(q_vec)
    # # sort by highest
    # cossimsorted = sorted(sim.items(), key=lambda x: x[1], reverse=True)
    # for k, v in cossimsorted:
    #     if v != 0.0:
    #         print("Cosine Similarities:", v)
    #         print()

    # postgreSQL_select_Query = "select * from results"
    # cursor.execute(postgreSQL_select_Query)
    # data = cursor.fetchall()
    # query = request.form['text']

    # cossim(query, df)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
