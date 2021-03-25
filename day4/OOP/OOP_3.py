
class bank:
    cid = 0
    cname = ""
    balance = 0

    def display(self):
        print("id =", self.cid)
        print("name =", self.cname)
        print("bank balance =", self.balance)


obja = bank()
objb = bank()
objc = bank()

obja.cid = 33

obja.display()
objb.display() 

# obja.display()
# bank.display(obja)  




