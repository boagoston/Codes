# Bruno Agoston - 126714

from ContiguityStack import ContiguityStack

class Nodo:
    def __init__(self, datum):
        self.datum = datum
        self.next = next

    def __repr__(self):
        return str(self.datum) + "-->" + str(self.next)


class ContiguityQueue:
    def __init__(self, size):
        self.queueArray = [None] * size
        self.bottomLimit = 0
        self.upperLimit = size - 1
        self.beginQueue = self.bottomLimit - 1 
        self.endQueue = self.upperLimit + 1
        self.size = size

    def isEmpty(self):
        return self.beginQueue < self.bottomLimit or self.endQueue > self.upperLimit

    def isFull(self):
        return (self.beginQueue == self.bottomLimit and self.endQueue == self.upperLimit) or (self.beginQueue == self.endQueue + 1) 
        

    def insert(self, datum):
        if (self.isEmpty()):
            self.beginQueue = self.bottomLimit
            self.endQueue = self.bottomLimit
            self.queueArray[self.endQueue] = datum
        elif (not self.isFull()):
            if (self.endQueue == self.upperLimit):
                self.endQueue = self.bottomLimit
            else:
                self.endQueue += 1
            self.queueArray[self.endQueue] = datum
        else: 
            print("A fila está cheia")

    def delete(self):
        if (not self.isEmpty()):
            if (self.beginQueue > self.endQueue and self.beginQueue == self.upperLimit):
                self.beginQueue = self.bottomLimit
            elif (self.beginQueue == self.endQueue):
                self.destroyQueue()
            else:
                self.beginQueue += 1
        

    def destroyQueue(self):
        self.beginQueue = self.bottomLimit - 1 
        self.endQueue = self.upperLimit + 1

    def consult(self):
        if (not self.isEmpty()):
            return self.queueArray[self.beginQueue]
            
    def __repr__(self):
        string = "["
        if (not self.isEmpty()):
            if (self.beginQueue <= self.endQueue):
                for i in range (self.beginQueue, self.endQueue +1):
                    string = string + " --> " + str(self.queueArray[i])
            else:
                for i in range (self.bottomLimit, self.endQueue +1):
                    string = string + " --> " + str(self.queueArray[i])
        return string + "]"

    


         

