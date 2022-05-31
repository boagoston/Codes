class Nodo:
    def __init__(self, data):
        self.data = data
        self.next_pointer = None


class lista_encadeada():
    def __init__(self):
        self.begin_list = None

    def insert_begin_of_list(self,position, data):
        
        if(position > 0):
            new_nodo = Nodo(data)
            if(position == 1):    
                new_nodo.next_pointer = self.begin_list
                self.begin_list = new_nodo
            else:
                aux_begin_list = self.begin_list
                i = 1
                while(i < position - 1 and aux_begin_list != None):
                    aux_begin_list = aux_begin_list.next_pointer
                    i += 1
                    if(aux_begin_list != None):
                        new_nodo.next_pointer = aux_begin_list.next_pointer
                        aux_begin_list.next_pointer = new_nodo

    def print_list(self):
        aux_begin_list = self.begin_list
        while (aux_begin_list != None):
            print("ID: " + aux_begin_list.data.ID + "\n Name: " + aux_begin_list.data.name + "\n Value: " + str(aux_begin_list.data.value) + "\n\n")
            aux_begin_list = aux_begin_list.next_pointer

    def find_position(self, value):
        aux_begin_list = self.begin_list
        i = 1
        while(aux_begin_list != None):
            if(aux_begin_list == value):
                return i
            aux_begin_list = aux_begin_list.next_pointer
        return False
    
    def find_value(self, position):
        if(position > 0):
            aux_begin_list = self.begin_list
            i = 1
            while (i < position and aux_begin_list != None):
                aux_begin_list = aux_begin_list.next_pointer
                i += 1
                if(i == position and aux_begin_list != None):
                    return aux_begin_list.info
        return False

    
    def remove_value(self, position):
        if (self.begin_list == None and position > 0):
            if (position == 1):
                self.begin_list = self.begin_list.next_pointer
            else:
                i = 1
                aux_begin_list = self.begin_list
                previous = None
                while (i < position and aux_begin_list != None):
                    previous = aux_begin_list
                    aux_begin_list = aux_begin_list.next_pointer
                    i+= 1
                if (aux_begin_list != None):
                    previous.next_pointer = aux_begin_list.next_pointer

    def clear_list(self):
        while(aux_begin_list != None):
            aux_begin_list = self.begin_list
            self.begin_list = self.begin_list.next_pointer
            aux_begin_list = None
        self.begin_list = None
