class Lista:
    def __init__(self,max):
        self.max = max
        self.vector = [None] * self.max
        self.start = -1
        self.end = -1

    def __repr__(self):
        string = "[begin \n"
        for i in range(self.start, self.end + 1):
            string = string + " --> " + str(self.vector[i]) 
        return string + "end]"
    
    def isListEmpty(self):
        return self.start == -1 or self.end == -1

    def getLength(self):
        if (self.isListEmpty()):
            return 0
        else:
            return self.end - self.start + 1

    def Insert(self, position, data):
        if self.max - 1 == self.end:
            print("Max value equal end of list")
            return False

        if((self.start != 0 or self.end != self.max - 1) and position > 0 and position <= self.getLength() + 1):
            if(self.isListEmpty()):
                self.start = 0
                self.end = 0
            elif (self.end != self.max -1):
                for i in range(self.end, self.start + position - 2, -1):
                    self.vector[i+1] = self.vector[i]
                    print("moveu")
                self.end = self.end + 1
            else:
                for i in range(self.start, self.start + position):
                    self.vector[i-1] = self.vector[i]
                    print("moveu")
                self.start = self.start - 1
            self.vector[self.start + position - 1] = data
            return True
        else:
            print("Invalid position")
            return False
    
    def Search(self, position):
        if not self.isListEmpty():
            if(position > 0 and position <= self.getLength() + 1):
                return self.vector[self.start + position - 1]
            else:
                print("Invalid position")
        else:
            print("Empty List")
            return False
    
    def ClearList(self):
        for i in range(self.start, self.end + 1):
            self.vector[i] = None
        self.start = -1 
        self.fim = -1

        return True
        
    
    def DeleteValue(self, position):
        if(position > 0 and position <= self.getLength() + 1):
            # for i in range(self.end, self.start + position - 2, -1):
            for i in range(self.start + position - 1, self.end):
                    self.vector[i] = self.vector[i+1]
                    self.vector[i+1] = None
                    print("moveu")
            self.end = self.end - 1
            return True
        return False
        
    
            


            
        
    
                