# sets
# unordered , no duplicates
# mutable
# members have to be immutable

seta = {'mangoes', 'bananas', 'mangoes', 'apples', 'melons', 'apples'}

setb = {'guavas', 'bananas', 'plums', 'apricots'}

print(seta)
print(setb)

seta.add('oranges') 

print(seta)

setc = {3, 5, "hi", (6, 7, 8)}
print(setc)

# error code
setd = {3, 5, "hi", [6, 7, 8]}
print(setd)
