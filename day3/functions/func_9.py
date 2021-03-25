# return any number of values 
# bydefault None 
 
def funca(la=33, lb=77, lc=99):
    le = la+lb+lc
    lf = la*2 + lb/10 + lc*3
    return le, lf, "hello"


x, y , z = funca()

print("return value, x =", x)
print("return value, y =", y)
print("return value, z =", z)


w = funca() 

print("return value, w =", w) 








