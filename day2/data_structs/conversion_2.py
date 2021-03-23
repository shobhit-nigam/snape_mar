# conversion

avengers = {'captain':'shield', 'ironman':'suit', 'hulk':['smash', 'science'], 'black widow':'energy'}
xmen = ['mystique', 'magneto', 'wolverine']
dc = ('wonder woman', 'batman', 'flash')

setdc = set(dc)

print("type of dc =", type(dc))
print("dc =", dc)
print("----\n")

print("type of setdc =", type(setdc))
print("setdc =",setdc)

print("----\n") 

lista = list(avengers) 
print("type of lista =", type(lista))
print("lista =", lista)

print("----\n") 

listb = list(avengers.values()) 
print("type of listb =", type(listb))
print("listb =", listb)
