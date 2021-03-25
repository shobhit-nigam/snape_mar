


fa = open("books.txt", "r")
stra = fa.read()
fa.close()

fb = open("words.txt", "w")
lista = stra.split()

for w in lista:
    fb.write(w)
    fb.write("\n")

