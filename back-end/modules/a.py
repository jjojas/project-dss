import json
import dijkstra as dj

g = {}

with open("book_data.json","r", encoding="utf8") as read_file:
    g = json.load(read_file)

# def getPath(passes: list, start: str, end:str) -> list:
#     list = []
#     if start=="13265773" and end=="20702993":
#         print("Found")
#     if (start in g) and (end in g):
#         if end in g[start]["recommend"]:
#             list.append(start)
#         else:
#             for key in g[start]["recommend"]:
#                 if key not in passes:
#                     passes.append(key)
#                     # print(f"{init} | {key} | {end} | {getPath(init,key,end)}")
#                     r = getPath(passes,key,end)
#                     if (len(r)!=0):
#                         list.append(key)
#                         list+=getPath(passes,key,end)
#                         break
#     print(list)
#     return list


# # a = []
# # for i in range(10):
# #     a.append(str(i))

# # print(a[:3])
# print(getPath(["364"],"364","20702993")[:-1])
# # print(getPath("a","a","c")[:-1])
# # print(getPath("a","a","d")[:-1])
# # print(getPath("a","a","e")[:-1])
# # print(getPath("a","a","f")[:-1])

print(dj.ShortestPath(g,"364","20702993")[1:-1])