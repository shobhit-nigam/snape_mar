
class bank:

    def __init__(self, i, n="john doe", b=0):
        self.cid = i
        self.cname = n
        self.balance = b
        print("successfully created bank account of", self.cname)

    def display(self):
        print("id =", self.cid)
        print("name =", self.cname)
        print("bank balance =", self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("successfully updated", self.cname, "balance")

    def withdraw(self, amount):
        if self.balance < amount:
            print("not enough balance")
            return

        self.balance = self.balance - amount
        print("successfully updated", self.cname, "balance") 

obja = bank(4800, "harry", 4000)
objb = bank(4802)
objc = bank(4804, "hermione", 5800)


obja.deposit(500)
obja.display()

objb.withdraw(800)
objb.display()