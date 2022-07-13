# Caio Beraldi Ribeiro - 11683


def sum(elemets):
    summed = 0
    for i in range(len(elemets)):
        summed = summed + elemets[i]
    return print("Soma iterativa:", summed)


def sum_recursion(elements):
    theSum = 0
    for i in elements:
        theSum = theSum + i
    return print("Soma recursiva:", theSum)


def factorial(number):
    factorial_sum = 1
    for i in range(2, number + 1):
        factorial_sum *= i
    return print("Fatorial iterativo:", factorial_sum)

def factorial_recursion(number):
    if number == 1:
        return 1
    else:
        return (number * factorial_recursion(number - 1))


def fibonacci(number):
    i = 0
    next_term = 1
    current = 1
    previous = 0
    while (i < number):
        next_term = current + previous
        current = previous
        previous = next_term
        i = i + 1
    return next_term

def fibonacci_recursion(number):    
    if number == 0:
        return 0
    elif number == 1 or number == 2:
        return 1
    else:
        return fibonacci_recursion(number-1) + fibonacci_recursion(number-2)


def digits_summed(number):
    if (number == 0 ):
        return 0
    else:
        return (number % 10) + digits_summed(number // 10)


        
    
#           Chamadas das Funções 


"""
Implemente de maneira iterativa e recursiva a operação soma_elementos(). 
Esse método deve receber como parâmetro uma lista ou vetor contendo números e retornar a soma dos elementos desta lista. Por exemplo, se v = [1, 2, 3, 10], soma_elementos(v) deve retornar 16.
""" 
elements = [1, 2 ,3, 10]
sum(elements)
sum_recursion(elements)


""" 
Implemente de maneira iterativa e recursiva um método que retorne o fatorial de um número natural passado como argumento. 

""" 
factorial(6)
print("Fatorial recursivo:", factorial_recursion(6))


""" 
Implemente de maneira iterativa e recursiva o cálculo de Fibonacci.
""" 
print("Fibonacci iterativo", fibonacci(6))
print("Fibonacci recursivo", fibonacci_recursion(6))


""" 
 Implemente de maneira recursiva o método soma_digitos(). 
 Este método recebe como parâmetro um número natural e retorna a soma dos dígitos. Por exemplo, soma_digitios(14) deve retornar 5.
""" 
print("Soma dos digitos recursivo", digits_summed(123))