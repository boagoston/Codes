import time


def fillVector(size_of_operators, operator_of_sequence):
    vector = [operator_of_sequence] * size_of_operators

    return vector

def printVector(vector):
    count = 1
    print("resultado: ", end="")
    for i in range(len(vector)):
        count += 1
        print(vector[i], end="")
        if(count % 3 == 0) and (i != len(vector)-1):
            print(".",end="")
        

def main():
    print("Digite quantos digitos sera o tamanho:")
#    size_of_operators = int(input())
    size_of_operators = 12800

    print("Digite o algarismo que será repetido no operador 1:")
    # operator_of_sequence1 = int(input())
    operator_of_sequence1 = 9
    print("Digite o algarismo que será repetido no operador 2:")
    # operator_of_sequence2 = int(input())
    operator_of_sequence2 = 9

    start_time = time.time()


    vector_operator1 = fillVector(size_of_operators, operator_of_sequence1)
    vector_operator2 = fillVector(size_of_operators, operator_of_sequence2)

    vector_result = [0] * (size_of_operators * 2)
    vector_result_aux = [0] * (size_of_operators + 1)
    len_vector_result = len(vector_result)

    for i in range(size_of_operators, 0, -1):
        aux_multiplication = 0
        for j in range(size_of_operators, 0, -1):
            aux_result = vector_operator1[j-1] * vector_operator2[i-1] + aux_multiplication
            vector_result_aux[j] = aux_result % 10
            aux_multiplication = aux_result // 10
        vector_result_aux[0] = aux_multiplication
        aux_multiplication = 0
        for j in range(size_of_operators+1, 0, -1):
            aux_sum = vector_result_aux[j-1] + vector_result[i+j-2] + aux_multiplication
            vector_result[i+j-2] = aux_sum % 10
            aux_multiplication = aux_sum // 10
        
    end_time = time.time()

    print("\nTempo total:", end_time - start_time)

    #printVector(vector_result)

main()