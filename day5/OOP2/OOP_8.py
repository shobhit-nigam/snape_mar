# repr
class sample:

    def __init__(self, a, b):
        self.data = a
        self.datab = b

    def display(self):
        print("data =", self.data, "and datab =", self.datab)

    def __repr__(self):
        return "object has data as "+str(self.data) 

    def __call__(self):
        print("the total data in this object is", self.data+self.datab)

objx = sample(100, 200)
objy = sample(50, 60)

objx.display()

print(objx)

print("----")
objx() 
