# dict
# nesting 

avengers = {'captain':'shield', 'ironman':'suit', 'hulk':['smash', 'science'], 'black widow':'energy'}
xmen = ['mystique', 'magneto', 'wolverine']
dc = {'wonder woman':'elegance', 'batman':'rich', 'flash':'fast'}


# print("avengers =", avengers)
marvel = {'avengers':avengers, 'xmen':xmen} 
superheroes = {'marvel':marvel, 'dc':dc} 

print("superheroes =", superheroes )
print("----\n")

print(avengers.keys())
print("----\n") 
print(avengers.values())
