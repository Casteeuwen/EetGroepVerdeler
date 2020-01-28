#from Lid import Lid

class Huis:
    def __init__(self, name):
        self.name = name
        self.tenants = []
        self.eaters = []
        self.cook = None

    def addTenant(self, lid):
        self.tenants.append(lid)

    def setCook(self, cook):
        self.cook = cook

    def getCook(self):
        return self.cook

    def hasCook(self):
        if self.cook != None:
            return True

    def addEater(self, lid):
        self.eaters.append(lid)

    def getTenants(self):
        return self.tenants

    def getName(self):
        return self.name

    def getEaters(self):
        return self.eaters