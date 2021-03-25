# read entire file
fa = open("books.txt", "r")

stra = fa.read()
print("read content is -->", stra)

print(len(stra))
