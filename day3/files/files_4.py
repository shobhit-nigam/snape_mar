


fa = open("books.txt", "r")
stra = fa.read(7)

print("read content is -->", stra)

print(fa.tell())

fa.seek(15)
stra = fa.read(7)

print("read content is -->", stra)

print(fa.closed)