# functions
# immutable
# stra is not a constant

stra = "toshiba"
strb = "koramangala madiwala"
strc = "toshiba"

print("stra =", id(stra))
print("strb =", id(strb))
print("strc =", id(strc))

strd = "TOSHIBA".lower() 

# 1000 lines of code, 3-4 running , 1gb of data 
stre = "toshiba" 

#   id(x) == id(y)  never 

print("strd =", id(strd))
print("stre =", id(stre))