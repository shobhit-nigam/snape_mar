# operator overloaded 

class time:
    def __init__(self, h=0, m=0):
        self.hours = h
        self.minutes = m

    def show(self):
        print(self.hours, "hour and", self.minutes, "minutes")

yest = time(1, 45)
today = time(1, 48)

yest.show()

total = time() 

# error code
total = yest + today 
