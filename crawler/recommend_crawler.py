# This crawler is book recommendation to crawl reviews data from LibraryThing
import psycopg2
import requests
import json
from bs4 import BeautifulSoup
import time

books = []
with open("books.txt", "r") as f:
    lines = f.read()
    books = lines.split("\n")

def getHTML(id):
    resp = requests.get(f"https://www.librarything.com/work/{id}",json.dumps({}))
    html = BeautifulSoup(resp.content, "html.parser") 
    return html

def recommendation_crawl(input,html):
    global conn
    cur = conn.cursor()
    recom = html.find("ol",{"class" : "memberrecommendations"})

    if recom != None:
        rcms = recom.find_all("li")

        for rcmd in rcms:
            span = rcmd.find("span",{"class" : "main"})
            upv = span.find("i",{"class" : "fa-thumbs-up"})
            if "<span" in upv.next_sibling :
                countUpvote = 0
            else:
                countUpvote = int(upv.next_sibling.string)
            dwv = span.find("i",{"class" : "fa-thumbs-down"})
            if "<span" in dwv.next_sibling :
                countDownote = 0
            else:
                countDownote = int(dwv.next_sibling.string)
            hyps = rcmd.find_all("a")
            for hyp in hyps:
                if hyp.has_attr('data-workid'):
                    id = hyp["data-workid"]
                    title = hyp["data-title"]
                    if (countUpvote - countDownote) > 1 :
                        cur.execute("INSERT INTO books(id,title) VALUES (%s,%s) ON CONFLICT DO NOTHING", (id,title))
                        cur.execute("INSERT INTO recommend VALUES (%s,%s,%s) ON CONFLICT DO NOTHING", (input,id,countUpvote-countDownote))
    else:
        print("No Recommendation")

if __name__ == "__main__":
    conn = psycopg2.connect(
    host="localhost",
    database="BookRecom",
    user="postgres",
    password="123456")

    start = time.time()
    for i in range(len(books)):
        try:
            print(f"Crawling {books[i]} recommendations",end= " | ")
            html = getHTML(books[i])
            recommendation_crawl(books[i],html)
            print(f"[{round(i*100/len(books),2)} %]", end="")
            print(f"[{round(time.time() - start,3)}] elapsed")
            conn.commit()
        except:
            pass
    conn.close()