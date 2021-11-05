# This crawler is created to crawl reviews data from LibraryThing
import psycopg2
import requests
import json
from bs4 import BeautifulSoup
import time

books = {}
data = {}
users = []

with open("user.txt", "r") as f:
    lines = f.read()
    users = lines.split("\n")

# with open("books2.json","r") as read_file:
#     books = json.load(read_file)

# with open("data.json","r") as read_file:
#     data = json.load(read_file)
        

def output():
    with open("user.txt", "w") as outfile:
        for user in users:
            outfile.write(user + "\n")

    with open("books2.json", "w") as outfile:
        json.dump(books, outfile)
    
    with open("data.json", "w") as outfile:
        json.dump(data, outfile)


# Crawl user list from available pages
def user_crawl():

    # This section fill crawl from MOST BOOKS in libraries
    resp = requests.get("https://www.librarything.com/zeitgeist/members/libraries",json.dumps({}))
    html = BeautifulSoup(resp.content, "html.parser")
    DataSelector = html.find("div",{"class" : "zsection colspan2"})
    usersCaptured = DataSelector.find_all("a")
    for User in usersCaptured:
        if " books" not in User.get_text():
            users.append(User.get_text())
    print(users)


def crawl_reviews(user):
    global books,conn
    cur = conn.cursor()
    cur.execute("INSERT INTO users VALUES (%s) ON CONFLICT DO NOTHING", (user,))
    # resp = requests.post("https://www.librarything.com/ajax_profilereviews.php",json.dumps(query))
    resp = requests.post(f"https://www.librarything.com/ajax_profilereviews.php?container=mainreviews&uniqueID=avc&view={user}")
    html = BeautifulSoup(resp.content, "html.parser")
    reviewsSelector = html.find_all("div",{"class" : "bookReview"})
    current = ""
    for review in reviewsSelector:
        section = review.find("div", {"class" :"commentHeader"})
        texts = section.find_all("a")
        for text in texts:
            # if text.has_attr('data-workid'):
            #     current = text['data-workid']
            #     if (current not in books) and (current != ""): 
            #         detail = {}
            #         detail['id'] = current
            #         detail['title'] = text['data-title']
            #         books[current] = detail
            #     if (user not in data):
            #         data[user] = []
            #     if (current not in data[user]):
            #         data[user].append(current)
            # else:
            #     if (current in books) and (current != ""): 
            #         books[current]["author"] = text.get_text()
            #         current = ""
            if text.has_attr('data-workid'):
                current = text['data-workid']
                cur.execute("INSERT INTO books(id,title) VALUES (%s,%s) ON CONFLICT DO NOTHING", (current,text['data-title'][:254],))
                cur.execute("INSERT INTO users_read VALUES (%s,%s) ON CONFLICT DO NOTHING", (user,current,))
            else:
                cur.execute("UPDATE books SET author = (%s) WHERE id=(%s)", (text.get_text(),current,))
                current = ""
    cur.close()


# user_crawl()
# output()

# load()
# print(users)
# for user in users:
#     crawl_reviews(user)

conn = psycopg2.connect(
    host="localhost",
    database="BookRecom",
    user="postgres",
    password="123456")

start = time.time()
for i in range(465,len(users)):
    try:
        print(f"Crawling {users[i]} reviews")
        crawl_reviews(users[i])
        print(f"[{round(i*100/len(users),2)} %]", end="")
        print("[",end="")
        box = round(i*20/len(users))
        print("*"*(box),end="")
        print("o"*(20-box),end="")
        print("] ",end="")
        print(f"[{round(time.time() - start,3)}] elapsed")
        conn.commit()
    except:
        pass
conn.close()