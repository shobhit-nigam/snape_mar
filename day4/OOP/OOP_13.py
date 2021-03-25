# shallow copy

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
objy = objx

objx.display()
print("--------")
objx.data = 111

objx.display()
print("--------")
objy.display()
