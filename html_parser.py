from bs4 import BeautifulSoup
import psycopg2

HOST = "localhost"
USERNAME = "postgres"
PASSWORD = "password"
DATABASE = "starter-server"
PORT = "5432"

db = psycopg2.connect(host=HOST, user=USERNAME, password=PASSWORD, database=DATABASE)
cursor = db.cursor()



with open("Pikachu Pokédex stats, moves, evolution & locations | Pokémon Database.html") as html_doc:
    soup = BeautifulSoup(html_doc, 'html.parser')
title_list = list()
url_list = list()
text_list = list()

title_list.append(soup.title.string)
# print(title_list[0])

for url in soup.find_all(property='og:url'):
    url_list.append(url.get('content'))
    # print(url.get('content'))
    # print(url_list)

text_list.append(soup.get_text())
print(text_list)

for index in range(0, len(title_list)):
    title = title_list[index]
    url = url_list[index]
    text = text_list[index]


    

    postgres_insert_query = """ INSERT INTO RESULTS (title, url, text) VALUES (%s,%s,%s)"""
    record_to_insert = (title,url,text)
    cursor.execute(postgres_insert_query, record_to_insert)
db.commit()