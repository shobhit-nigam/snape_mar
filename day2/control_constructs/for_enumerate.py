# range vs enumerate

lista = ['cc', 'gg', 'tt', 'dd', 'jj', 'ww']

for val in enumerate(lista):
    print("val =", val)




for val in enumerate(lista, 50):
    print("val =", val)