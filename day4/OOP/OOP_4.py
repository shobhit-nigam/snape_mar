
class bank:
    cid = 0
    cname = ""
    balance = 0

    def display(self):
        print("id =", self.cid)
        print("name =", self.cname)
        print("bank balance =", self.balance)

    def update(self, i, n, b):
        self.cid = i
        self.cname = n
        self.balance = b
        print("successfully updated", self.cname, "records")



obja = bank()
objb = bank()
objc = bank()

# bank itself is an object
# print(type(obja))
# print(type(bank))

obja.update(23980, "harry", 5000)
objb.update(23982, "ron", 4000)

obja.display()
objb.display() 
objc.display()

# obja.display()
# bank.display(obja)  




