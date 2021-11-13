import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="BookRecom",
    user="postgres",
    password="123456")

cur = conn.cursor()

user = "Test"
cur.execute("INSERT INTO users VALUES (%s)", (user,))
cur.close()
conn.commit()
conn.close()