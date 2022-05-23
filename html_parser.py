from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import text
import pandas as pd
from bs4 import BeautifulSoup
import psycopg2
import os
import numpy as np
import re
import operator
import sys
import csv
import pickle

from sqlalchemy import desc

csv.field_size_limit(sys.maxsize)

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
            desc_list = list()

            title_list.append(soup.title.string)
            
            for url in soup.find_all(rel='canonical'):
                url_list.append(url.get('href'))

                inputtext=soup.find("body").text.replace("\t", " ").replace("\r", " ").replace("\n", "").replace("^", " ")
                text_list.append(inputtext)

                content = soup.select('p')
                sentences = str()
                periods = 0
                description_amount = 3 - periods
                for i in content:
                    matches = re.findall(r'(.+?[.!])(?: |$)', i.getText())
                    total_sentences = len(matches)
                    for i in range(min(total_sentences, description_amount)):
                        periods = sentences.count('.')
                        sentences = sentences.replace("^", " ") + (matches[i]) + " "
                        periods = sentences.count('.')
                    if periods >= 3:
                        break
                desc_list.append(sentences.replace("^", " "))

            for index in range(0, len(title_list)):
                title = title_list[index]
                url = url_list[index]
                textdata = text_list[index]
                descdata = desc_list[index]
                postgres_insert_query = """INSERT INTO RESULTS (title, url, description, text) VALUES (%s,%s,%s,%s);"""
                record_to_insert = (title,url,descdata, textdata)
                cursor.execute(postgres_insert_query, record_to_insert)
            db.commit() # uncomment to actually write to database server.

copy_query = "COPY results TO 'data.csv'  WITH DELIMITER '^' CSV HEADER;"
fout = open('data.csv', 'w')
cursor.copy_to(fout, 'results', sep="^")
col_names = ["id", "title", "url", "description", "text"]
df = pd.read_csv('data.csv', encoding='utf-8', sep='^', names=col_names, error_bad_lines=False, engine='python')
df.head()
df.to_pickle('data.pkl') 
#save to pickle for faster loading and use in app.py