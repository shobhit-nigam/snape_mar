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
print("superheroes['marvel'] =", superheroes['marvel'] )
print("----\n")
print("superheroes['marvel']['avengers'] =", superheroes['marvel']['avengers'] )
print("----\n")
print("superheroes['marvel']['avengers']['hulk'] =", superheroes['marvel']['avengers']['hulk'] )
print("----\n")
print("superheroes['marvel']['avengers']['hulk'][0] =", superheroes['marvel']['avengers']['hulk'][0] )   
print("----\n")
print("superheroes['marvel']['avengers']['hulk'][0][1] =", superheroes['marvel']['avengers']['hulk'][0][1] )   

