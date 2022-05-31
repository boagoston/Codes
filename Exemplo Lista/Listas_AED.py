class Lista:
    def __init__(self,max):
        self.max = max
        self.vetor = [None] * self.max
        self.inicio = -1
        self.fim = -1

    def __repr__(self):
        string = "[ini "
        for i in range (self.inicio, self.fim + 1):
            string = string + " --> " + str(self.vetor[i])
        return string + "]"

    def isEmpty(self):
        return self.inicio == -1 or self.fim == -1
    
    def Length(self):
        if self.isEmpty():
            return False
        else:
            return self.fim - self.inicio + 1

    def Inserir(self, posicao, data):
        # verificar se existe espaço e se a posição é valida
        if ((self.inicio != 0 or self.fim != self.max - 1) and posicao > 0 and posicao <= self.Length() + 1):
            if (self.isEmpty()):
                self.inicio = 0
                self.fim = 0
            elif (self.fim != self.max - 1): # se tem espaço, desloca para o fim
                for i in range (self.fim, self.inicio + posicao - 2, -1):
                    self.vetor[i+1] = self.vetor[i]
                    print("moveu")
                self.inicio = self.inicio - 1
            self.vetor[self.inicio + posicao - 1] = data
            return True
        else:
            return False

    def Consultar(self, posicao):
        if not self.isEmpty():
            return self.vetor[self.inicio + posicao - 1]
    
    def Limpar(self):
        self.inicio = -1
        self.fim = -1

    def Excluir(self):
        #fazer
        pass

    def InserirOtimizado(self, posicao, data):
        pass

    



