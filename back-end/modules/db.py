import psycopg2
from py2neo import Graph, Node, Relationship, NodeMatcher

def connect_neo():
    g = Graph("bolt://localhost:7687",auth=("neo4j","123456"))
    return g


def connect_psql():
    conn = psycopg2.connect(
        host="localhost",
        database="BookRecom",
        user="postgres",
        password="123456")
    return conn

def get(db,table):
    cur = db.cursor()
    cur.execute(f"SELECT * FROM {table};")
    return cur.fetchall()

def books_get_tags(db,id):
    cur = db.cursor()
    cur.execute(f"select tag from tags where book='{id}';")
    return cur.fetchall()

def books_get_title(db,id):
    cur = db.cursor()
    cur.execute(f"select title,author from books where id='{id}';")
    return cur.fetchall()

def books_get_recom(db,id):
    cur = db.cursor()
    cur.execute(f"(select recom as target from recommend where origin='{id}') union (select origin as target from recommend where recom='{id}');")
    return cur.fetchall()