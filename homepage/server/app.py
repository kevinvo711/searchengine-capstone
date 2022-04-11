from flask import Flask
from flask import request
import json
from flask import jsonify
import psycopg2
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/flask', methods=['GET'])
def index():
    return "Flask server"



#connect to database
HOST = "localhost"
USERNAME = "postgres"
PASSWORD = "password"
DATABASE = "starter-server"
PORT = "5432"

db = psycopg2.connect(host=HOST, user=USERNAME,
                      password=PASSWORD, database=DATABASE)
cursor = db.cursor()

@app.route('/test', methods=['POST', 'GET'])
def cossim(q, df):
    #vectorize search term
    q = [q] 
    q_vec = TfidfVectorizer().transform(q).toarray().reshape(df.shape[0],)
    sim = {}
    # calculate cossim
    for i in range(10):
        sim[i] = np.dot(df.loc[:, i].values, q_vec) / np.linalg.norm(df.loc[:, i]) * np.linalg.norm(q_vec)
    # sort by highest
    cossimsorted = sorted(sim.items(), key=lambda x: x[1], reverse=True)
    for k, v in cossimsorted:
        if v != 0.0:
            print("Cosine Similarities:", v)
            print()
query = request.form.get('text')

postgreSQL_select_Query = "select * from results"
cursor.execute(postgreSQL_select_Query)
data = cursor.fetchall()
  
cossim(query, df)


if __name__ == "__main__":
    app.run(port=8000, debug=True)


    