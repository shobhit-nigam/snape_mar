
fa = open("books.txt", "r")

stra = fa.read(6)
print(type(stra))

print("read content is -->", stra)

stra = fa.read(7)
print("read content is -->", stra)
