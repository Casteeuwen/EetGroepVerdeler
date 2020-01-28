from Huis import Huis

class Lid:
    def __init__(self, name, home, anci, eetMee, phoneNumber):
        self.name = name
        self.anci = anci
        self.home = home
        self.eetMee = eetMee
        self.phoneNumber = phoneNumber

    def getEetMee(self):
        return self.eetMee

    def getName(self):
        return self.name

    def getHome(self):
        return self.home

    def getAnci(self):
        return self.anci

    def getAnci(self):
        return self.anci

    def setEetMee(self, value):
        self.eetMee = value

    def __str__(self):
        return "%s %s %s"%(self.name, self.anci, self.home)
        #self.name," ",self.anci," ",self.home