# This program will get all the books that people recommend from the input
# It will also search for books that connects between the input
# @author: Justin Dermawan Ikhsan

# import db
import re
from . import dijkstra as d
# from . import db
import json
# from py2neo import Graph, Node, Relationship, NodeMatcher

# neo = db.connect_neo()
# psql = db.connect_psql()

tagDump = []
titleDump = []
idDump = []
booksDump = {}
with open("modules/book_data.json","r", encoding="utf8") as read_file:
    booksDump = json.load(read_file)

for book in booksDump:
    idDump.append(book)
    titleDump.append(booksDump[book]['title'])
    for tag in booksDump[book]['tags']:
        if tag not in tagDump:
            tagDump.append(tag)

def recommend(tagsinput: list,books: list) -> dict:
    '''
    Get JSON data of all the books that are recommended by the system

    Parameters:

    tags(list) : All the tags filtered by the user
    books(list) : All the books that read by the user
    '''

    recomlist = []
    if len(books)>3:
        spath = []
        for i in range(len(books)):
            for j in range(len(books)):
                if i>j:
                    for item in d.ShortestPath(booksDump,books[i],books[j]):
                        spath.append(item)
        max = -1
        for item in list(set(spath)):
            if (spath.count(item))>max:
                max = spath.count(item)
        for item in list(set(spath)):
            if (spath.count(item))>=max-1:
                recomlist.append(item)
    elif len(books)>1:
        spath = []
        for i in range(len(books)):
            for j in range(len(books)):
                if i>j:
                    for item in d.ShortestPath(booksDump,books[i],books[j]):
                        spath.append(item)
        for item in list(set(spath)):
            recomlist.append(item)
        # q = "MATCH "
        # for i in range(len(books)):
        #     q+="(" + chr(97+i) + ":Book {id: '" + books[i] + "'}),"
        # ct = 0
        # for i in range(len(books)):
        #     for j in range(len(books)):
        #         if i>j:
        #             ct+=1
        #             q+="path" + str(ct) + "=shortestPath((" + chr(97+i) + ")-[:RECOMMEND*]-(" + chr(97+j) + ")),"
        # q = q[:-1]
        # q+=" RETURN "
        # for i in range(ct):
        #     q+="nodes(path"+str(i+1)+"),"
        # q = q[:-1]
        # a = neo.run(q).data()
        # if len(a)>0:
        #     for key in a[0] :
        #         for node in a[0][key]:
        #             recomlist.append(node['id'])

    elif len(books)==1:
        recomlist.append(books[0]["recommend"])

    else:
        for book in booksDump:
            if any(x in tagsinput for x in booksDump[book]["tags"]):
                recomlist.append(book)
    
    finalrec = {}
    for recom in recomlist:
        if len(tagsinput)>0:
            if any(x in tagsinput for x in booksDump[recom]["tags"]):
                finalrec[recom] = booksDump[recom]
        else:
            finalrec[recom] = booksDump[recom]

    return finalrec

def searchTag(q: str) -> list:
    r = re.compile(f".*{q}")
    tags = list(filter(r.match, tagDump))
    return tags[:10]

def searchName(q: str) -> list:
    d = []
    r = re.compile(f".*{q}")
    titles = list(filter(r.match, titleDump))
    for title in titles:
        id = searchIDfromName(title)
        item = {}
        item['id'] = id
        item['name'] = title
        d.append(item)
    return d[:10]

def searchIDfromName(q: str) -> str:
    if q in titleDump:
        return titleDump.index(q)
    else:
        return ''

if __name__ == "__main__":
    a  = ['love','classics']
    b1 = []
    b2 = ["20702993","5400850","819161"]
    c3 = ["364"]
    print(recommend(b1,b2))
    # print(recommend(a,b1))
    # print(recommend(b1,c3))
    # print(recommend(a,c3))
    # print(searchName("to"))