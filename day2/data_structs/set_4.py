# sets
# unordered , no duplicates
# mutable
# members have to be immutable

seta = {'mangoes', 'bananas', 'mangoes', 'apples', 'melons', 'apples'}

setb = {'guavas', 'bananas', 'plums', 'apricots'}

print("seta =", seta)
print("setb =", setb)

print("union = ", seta | setb)
print("intersection = ", seta & setb)
print("diff = ", seta - setb)
print("symmetric diff  = ", seta ^ setb) 
