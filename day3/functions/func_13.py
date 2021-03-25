# return any number of values 
# bydefault None 
 
# global 
# local 


# global
ga = 100
print("outside ga =", ga)

def funca():
    global ga
    la = 11
    ga = 22
    print("in function ga =", ga)
    print("in function la =", la)

funca()

# global
print("outside ga =", ga)

# inner functions 
def funcc():
    # 
    # 
    def funcd():
        # 
        #
        pass
    # 
    # 
    pass





