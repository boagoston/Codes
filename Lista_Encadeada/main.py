from Product import *
from lista_encadeada import *

productA = Product("1","Monitor", 500)
productB = Product("2","Teclado", 100)
productC = Product("3","mouse", 40)
productD = Product("4","HD", 350)

lista = lista_encadeada()

lista.insert_begin_of_list(1,productA)
lista.print_list()

lista.insert_begin_of_list(2,productB)
lista.print_list()


lista.insert_begin_of_list(3,productC)
lista.print_list()


lista.insert_begin_of_list(4,productD)
lista.print_list()


search_product = lista.find_position(productC)
print("Result of search is: \n" + str(search_product))
search_product = lista.find_value(2)

lista.remove_value(2)
lista.print_list()

lista.DeleteValue(1)
lista.print_list()


print("Executando processado para limpar lista:")
print("Lista anterior:\n" + str(lista))
lista.clear_list()
print("Lista depois da limpeza:\n" + str(lista))
    
