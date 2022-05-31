from Carro import *
from Listas_AED import *

carroA = Carro("AAA1234", 2020)
carroB = Carro("BBB0987", 2009)
carroC = Carro("CCC4567", 1985)

lista = Lista(5)

if (lista.Inserir(1,carroA)):
    print(lista)
if (lista.Inserir(1,carroA)):
    print(lista)
if (lista.Inserir(1,carroA)):
    print(lista)
if (lista.Inserir(1,carroA)):
    print(lista)
if (lista.Inserir(1,carroA)):
    print(lista)
if (lista.Inserir(1,carroA)):
    print(lista)


meuCarro = lista.Consultar(5)
print(meuCarro)