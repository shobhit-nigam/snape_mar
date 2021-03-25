# inheritance

class unix:
    def __init__(self):
        print("init of unix")

    def cmd(self):
        print("great command line")

class linux(unix):
    def __init__(self):
        print("init of linux")

    def free(self):
        print("free & open source")



obju = unix()
objl = linux()

objl.cmd()
objl.free()