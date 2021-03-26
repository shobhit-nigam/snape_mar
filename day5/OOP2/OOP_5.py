# operator overloaded 
# chaining 

class time:
    def __init__(self, h=0, m=0):
        self.hours = h
        self.minutes = m

    def show(self):
        print(self.hours, "hour and", self.minutes, "minutes")

    def __add__(self, other):
        min_1 = self.hours * 60 + self.minutes
        min_2 = other.hours * 60 + other.minutes 
        totmin = min_1 + min_2 

        temp = time()
        temp.hours = totmin//60 
        temp.minutes = totmin%60 

        return temp


yest = time(1, 45)
today = time(1, 48)
wed = time(3, 33)

# yest.show()

total = time() 

# error code
total = yest + today + wed

total.show()
