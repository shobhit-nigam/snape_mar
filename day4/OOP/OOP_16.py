# inheritance
# multilevel 
# multiple

class unix:
    def cmd(self):
        print("great command line")

class linux(unix):
    def free(self):
        print("free & open source")

class mobileOS():
    def portable(self):
        print("can be ported to mini devices")

class android(linux, mobileOS):
    def ui():
        print("great GUI")


obju = unix()
objl = linux()
obja = android()

obja.cmd()