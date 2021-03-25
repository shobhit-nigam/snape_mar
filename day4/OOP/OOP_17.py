# inheritance
# multilevel 
# multiple

class unix:
    def cmd(self):
        print("great command line")

class linux(unix):
    def free(self):
        print("free & open source")

    def flexible(self):
        print("linux is flexible")

class mobileOS():
    def portable(self):
        print("can be ported to mini devices")

    def flexible(self):
        print("mobileOS is flexible")


class android(mobileOS, linux):
    def ui(self):
        print("great GUI")


obju = unix()
objl = linux()
obja = android()

obja.flexible()