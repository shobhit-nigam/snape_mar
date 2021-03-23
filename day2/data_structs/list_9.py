# lists
# nesting

avengers = ['captain', 'ironman', 'hulk', 'black widow', 'Thor', 'Wanda', 'marvel']
xmen = ['mystique', 'magento']
marvel = [avengers, xmen]

superheroes = [marvel, 'spiderman', 'batman']

listc = ['hi', 4, 6, [1.9, 3.2, 6.7], ["hi", "hello", "howdy"], 45]

print(marvel)
print(marvel[0])
print(marvel[0][1])
print(marvel[0][1][2]) 

# allowed:
marvel[0][1] = 24

# error code:
marvel[0][1][2] = 't'
