from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import text
import pandas as pd
from bs4 import BeautifulSoup
import psycopg2
import os
import numpy as np
import re
import operator
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import defaultdict
from nltk.corpus import wordnet as wn

HOST = "localhost"
USERNAME = "postgres"
PASSWORD = "password"
DATABASE = "starter-server"
PORT = "5432"

db = psycopg2.connect(host=HOST, user=USERNAME,
                      password=PASSWORD, database=DATABASE)
cursor = db.cursor()


path = r"wikipedia/en.wikipedia.org"
for filename in os.listdir(path):
        if filename.endswith(".html"):
            fullpath = os.path.join(path, filename)
            soup = BeautifulSoup(open(fullpath), 'lxml')
            title_list = list()
            url_list = list()
            text_list = list()

            title_list.append(soup.title.string)
            # print(title_list[0])

            for url in soup.find_all(rel='canonical'):
                url_list.append(url.get('href'))
                # print(url.get('href'))
                # print(url_list)
                inputtext=soup.find("body").text.replace("\t", "").replace("\r", "").replace("\n", "").replace("^", "")
            # print(inputtext)

            # tfIdfVectorizer = TfidfVectorizer(
            #     use_idf=True, stop_words=text.ENGLISH_STOP_WORDS)
            # tfIdf = tfIdfVectorizer.fit_transform(inputtext)
            # df = pd.DataFrame(tfIdf[0].T.todense(
            # ), index=tfIdfVectorizer.get_feature_names_out(), columns=["TF-IDF"])
            # df = df.sort_values('TF-IDF', ascending=False)
            # dftojson = df.to_json(orient="columns")
            text_list.append(inputtext)
            # print(text_list)
            # print (dftojson)

            for index in range(0, len(title_list)):
                title = title_list[index]
                url = url_list[index]
                textdata = text_list[index]
                # print(text)
                postgres_insert_query = """ INSERT INTO RESULTS (title, url, text) VALUES (%s,%s,%s)"""
                record_to_insert = (title,url,textdata)
                cursor.execute(postgres_insert_query, record_to_insert)
            db.commit()
            # uncomment to actually write to database server.

