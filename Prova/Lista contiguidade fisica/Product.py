class Product:
    def __init__(self, ID, name, value):
        self.ID = ID
        self.name = name
        self.value = value

    def __repr__(self):
        return "ID: " + self.ID + "\n Name: " + self.name + "\n Value: " + str(self.value) + "\n"

    def getID(self):
        return self.ID
    
    def getName(self):
        return self.name
    
    def getValue(self):
        return self.value

    def setName(self,name):
        self.name = name
    
    def setValue(self, value):
        self.value = value

    