# lists
# references even in nesting

avengers = ['captain', 'ironman', 'hulk', 'black widow', 'Thor', 'Wanda', 'marvel']
xmen = ['mystique', 'magento']
marvel = [avengers, xmen]

superheroes = [marvel, 'spiderman', 'batman']

heroes = avengers.copy() 
print("avengers =", avengers)
print("heroes =", heroes)

heroes.reverse()
heroes.pop()
heroes.sort()
heroes.sort()

print("after editing heroes")
print("avengers =", avengers)
print("heroes =", heroes)


