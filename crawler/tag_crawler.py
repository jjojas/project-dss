
from bs4.element import Tag
import psycopg2
import requests
import json
from bs4 import BeautifulSoup
import time

books = []
with open("books.txt", "r") as f:
    lines = f.read()
    books = lines.split("\n")

def getPage(id):
    resp = requests.get(f"https://www.librarything.com/work/{id}")
    html = BeautifulSoup(resp.content, "html.parser") 
    script = html.find("script",{"data-source" : "inc_librarything.print_scriptlines_lt1.1"})
    getter = (str(script)).split(f"ajax_work_makeworkCloud({id}, ")[1].split(")")[0]
    return getter
    
def getHTML(id,check):
    resp = requests.post(f"https://www.librarything.com/ajax_work_makeworkCloud.php?work={id}&check={check}")
    html = BeautifulSoup(resp.content, "html.parser") 
    return html

def tag_crawl(id,html):
    global conn
    cur = conn.cursor()
    
    tags =  html.div.find_all("span",{"class" : "tag"})
    for tag in tags:
        cat = tag.a.get_text()
        count = int(str(tag.span.get_text()).replace("(","").replace(")","").replace(",",""))
        if count>100:
            cur.execute("INSERT INTO tags VALUES (%s,%s,%s) ON CONFLICT DO NOTHING", (id,cat,count))

if __name__ == "__main__":
    conn = psycopg2.connect(
    host="localhost",
    database="BookRecom",
    user="postgres",
    password="123456")

    start = time.time()
    for i in range(len(books)):
        try:
            print(f"Crawling {books[i]} reviews",end= " | ")
            html = getHTML(books[i],getPage(books[i]))
            tag_crawl(books[i],html)
            print(f"[{round(i*100/len(books),2)} %]", end="")
            print(f"[{round(time.time() - start,3)}] elapsed")
            conn.commit()
        except:
            pass
    conn.close()