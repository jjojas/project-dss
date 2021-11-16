import json
import db


psql = db.connect_psql()

books = {}
def output():
    with open("book_data.json", "w") as outfile:
        json.dump(books, outfile)

def populate(data: list) -> dict:
    finalrec = {}
    for recom in data:
        titlefromdb = db.books_get_title(psql,recom)
        title = titlefromdb[0][0].replace("-"," ")
        author = titlefromdb[0][1]

        tagsfromdb = db.books_get_tags(psql,recom)
        tags = []

        if len(tagsfromdb) > 0 :
            for tagfromdb in tagsfromdb:
                tags.append(tagfromdb[0])
        
        recoms = []
        recomfromdb = db.books_get_recom(psql,recom)
        if len(recomfromdb) > 0 :
                    for recomA in recomfromdb:
                        recoms.append(recomA[0])
    
        finalrec[recom] = {}
        finalrec[recom]["id"] = recom
        finalrec[recom]["title"] = title
        finalrec[recom]["author"] = author
        finalrec[recom]["tags"] = tags
        finalrec[recom]["recommend"] = recoms

    return finalrec

l = []
for data in db.uniqueBook(psql):
    l.append(data[0])
books = populate(l)
output()

    