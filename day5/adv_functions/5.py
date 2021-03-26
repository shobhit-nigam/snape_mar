# map

lista = ['a', 'y', 't', 'e', 'i', 'f', 'r', 'w', 'v', 'o', 'a'] 
lista = [5, 8, 2, 4, 9, 1, 4, 6, 7]
listb = [2, 3, 6, 4, 7, 9, 8, 1, 5]


def funca(la, lb):
    lc = la*2 + lb 
    return lc


res = list(map(funca, lista, listb)) 

print(res) 

