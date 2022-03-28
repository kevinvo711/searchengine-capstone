from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import text
import pandas as pd
from bs4 import BeautifulSoup
import psycopg2
import os

HOST = "localhost"
USERNAME = "postgres"
PASSWORD = "password"
DATABASE = "starter-server"
PORT = "5432"

db = psycopg2.connect(host=HOST, user=USERNAME, password=PASSWORD, database=DATABASE)
cursor = db.cursor()


path = r"wikipedia/en.wikipedia.org"
for filename in os.listdir(path):
        if filename.endswith(".html"):
            fullpath = os.path.join(path, filename)
            soup = BeautifulSoup(open(fullpath), 'html.parser')
            title_list = list()
            url_list = list()
            text_list = list()

            title_list.append(soup.title.string)
            # print(title_list[0])

            for url in soup.find_all(rel='canonical'):
                url_list.append(url.get('href'))
                # print(url.get('href'))
                # print(url_list)
            inputtext = [soup.get_text()]

            

            tfIdfVectorizer=TfidfVectorizer(use_idf=True, stop_words=text.ENGLISH_STOP_WORDS)
            tfIdf = tfIdfVectorizer.fit_transform(inputtext)
            df = pd.DataFrame(tfIdf[0].T.todense(), index=tfIdfVectorizer.get_feature_names_out(), columns=["TF-IDF"])
            df = df.sort_values('TF-IDF', ascending=False)
            dftojson = df.to_json(orient ="columns")
            text_list.append(dftojson)
            # print(text_list)

            # print (dftojson)

            for index in range(0, len(title_list)):
                title = title_list[index]
                url = url_list[index]
                tfidf = text_list[index]
                # print(text)

                postgres_insert_query = """ INSERT INTO RESULTS (title, url, text) VALUES (%s,%s,%s)"""
                record_to_insert = (title,url,tfidf)
                cursor.execute(postgres_insert_query, record_to_insert)
            db.commit()