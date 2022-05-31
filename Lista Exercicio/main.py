from AED.Lista_Encadeada.Product import *
from Lista import *

productA = Product("1","Monitor", 500)
productB = Product("2","Teclado", 100)
productC = Product("3","mouse", 40)
productD = Product("4","HD", 350)

lista = Lista(10)

if(lista.Insert(1,productA)):
    print(lista)
else:
    print("FAIL INSERT")

if(lista.Insert(2,productB)):
    print(lista)
else:
    print("FAIL INSERT")

if(lista.Insert(3,productC)):
    print(lista)
else:
    print("FAIL INSERT")

if(lista.Insert(4,productD)):
    print(lista)
else:
    print("FAIL INSERT")    


search_product = lista.Search(3)

if(search_product != None):
    print("Result of search is: \n" + str(search_product))
else:
    print("FAIL SEARCH")

if(lista.DeleteValue(1)):
    print(lista)
else:
    print("FAIL DELETE")

if(lista.DeleteValue(4)):
    print(lista)
else:
    print("FAIL DELETE")

if(lista.ClearList()):
    print("List clear successfully")
    print(lista)
else:
    print("FAIL CLEAR ")
    
