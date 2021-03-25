# private __ 
# encapsulation 

class A:
    data = 100
    _datb = 200
    __datc = 300
    __datd__ = 400

    def display(self):
        print("data =", self.data)
        print("_datb =", self._datb)
        print("__datc =", self.__datc)
        print("__datd__ =", self.__datd__)

objx = A()
#objx.display()

print("data =", objx.data)
print("_datb =", objx._datb)
# error 
#print("__datc =", objx.__datc)
print("__datd__ =", objx.__datd__)