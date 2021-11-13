import psycopg2
from py2neo import Graph, Node, Relationship, NodeMatcher


books = []
with open("books.txt", "r") as f:
    lines = f.read()
    books = lines.split("\n")


def detail(conn,id):
    cur = conn.cursor()
    cur.execute(f"select title from books where id='{id}'")
    return cur.fetchall()[0][0].replace("-"," ")


if __name__ == "__main__":
    conn = psycopg2.connect(
    host="localhost",
    database="BookRecom",
    user="postgres",
    password="123456")

    cur = conn.cursor()
    cur.execute("select * from tags;")
    a = cur.fetchall()
    # print(a[0][0])

    g = Graph("bolt://localhost:7687",auth=("neo4j","123456"))
    matcher = NodeMatcher(g)
    for data in a:
        idB,tag,val = data

        if matcher.match("Tag", name=tag).first():
            tagNode = matcher.match("Tag", name=tag).first()
        else:
            tagNode = Node("Tag", name=tag)
            g.create(tagNode)
        
        book = matcher.match("Book", id =idB).first()
        if book:
            rel = Relationship(book,"TAG",tagNode,value=val)
            g.create(rel)

        # # Name Updater
        # exists = matcher.match("Book",id = idB).first()
        # if exists:
        #     exists['name'] = detail(conn,idB)
        #     g.push(exists)



        ## Relationship Matcher
        # if matcher.match("Book", id=a[i][0]).first():
        #     main = matcher.match("Book", id=a[i][0]).first()
        # else:
        #     main = Node("Book", id = a[i][0])
        #     g.create(main)
        # if matcher.match("Book", id=a[i][1]).first():
        #     recom = matcher.match("Book", id=a[i][1]).first()
        # else:
        #     recom = Node("Book", id = a[i][1])
        #     g.create(recom)
        # rel = Relationship(main,"RECOMMEND",recom,value=a[i][2])
        # g.create(rel)
    

