# This program will get all the books that people recommend from the input
# It will also search for books that connects between the input
# @author: Justin Dermawan Ikhsan

# import db
from . import db
from py2neo import Graph, Node, Relationship, NodeMatcher

neo = db.connect_neo()
psql = db.connect_psql()

def recommend(tagsinput: list,books: list) -> dict:
    '''
    Get JSON data of all the books that are recommended by the system

    Parameters:

    tags(list) : All the tags filtered by the user
    books(list) : All the books that read by the user
    '''

    recomlist = []
    if len(books)>1:
        q = "MATCH "
        for i in range(len(books)):
            q+="(" + chr(97+i) + ":Book {id: '" + books[i] + "'}),"
        ct = 0
        for i in range(len(books)):
            for j in range(len(books)):
                if i>j:
                    ct+=1
                    q+="path" + str(ct) + "=shortestPath((" + chr(97+i) + ")-[:RECOMMEND*]-(" + chr(97+j) + ")),"
        q = q[:-1]
        q+=" RETURN "
        for i in range(ct):
            q+="nodes(path"+str(i+1)+"),"
        q = q[:-1]
        a = neo.run(q).data()
        for key in a[0] :
            for node in a[0][key]:
                recomlist.append(node['id'])

    else:
        q ="MATCH (a:Book {id: '" + books[0] + "' })-[r:RECOMMEND]-(b) RETURN b"
        a = neo.run(q).data()
        for key in a :
            recomlist.append(key["b"]["id"])
    
    finalrec = {}
    for recom in recomlist:
        titlefromdb = db.books_get_title(psql,recom)
        title = titlefromdb[0][0].replace("-"," ")
        author = titlefromdb[0][1]

        tagsfromdb = db.books_get_tags(psql,recom)
        tags = []
        if len(tagsfromdb) > 0 :
            for tagfromdb in tagsfromdb:
                tags.append(tagfromdb[0])

        if len(tagsinput)>0:
            if any(x in tagsinput for x in tags):
                finalrec[recom] = {}
                finalrec[recom]["id"] = recom
                finalrec[recom]["title"] = title
                finalrec[recom]["author"] = author
                finalrec[recom]["tags"] = tags
        else:
            finalrec[recom] = {}
            finalrec[recom]["id"] = recom
            finalrec[recom]["title"] = title
            finalrec[recom]["author"] = author
            finalrec[recom]["tags"] = tags


    return finalrec

if __name__ == "__main__":
    a  = []
    b = ["20702993","364","5400850","819161"]
    c = ["364"]
    print(recommend(a,b))
