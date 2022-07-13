def sum():
    print("Sum")
    value01 = input("Please enter a string:\n")
    value02 = input("Please enter a string:\n")
    value01 = str(value01)
    value02 = str(value02)
    sum_result = []
    v_value01 = []
    v_value02 = []    
    unity_ten = 0
    sum_insede = 0
    m = 0
    
    if(len(value01) > len(value02)): 
        size = len(value01) + 1 
    else: 
        size = len(value02) + 1 
    
    size = size + 1 

    while(len(value01) != size): 
        value01 = '0' + value01 
    while(len(value02) != size): 
        value02 = '0' + value02      
    for i in range(size): 
        sum_result.append(0) 

    
    for i in range(size):
        m = value01[i]
        v_value01.append(int(m))
       

    for i in range(size):
        m = value02[i]
        v_value02.append(int(m))


    print("Vetor resultado vazio: ", sum_result)
    print("Primeiro vetor: ", v_value01)
    print("Segundo vetor: ", v_value02)
    print("Tamanho igual a: ", size)
    print('----------------------- // -----------------------')

    for i in range(size - 1, -1, -1):
        if(unity_ten > 0):
            sum_insede = (v_value01[i] + v_value02[i]) + unity_ten
            if(sum_insede>9):
                sum_result[i] = sum_insede % 10
            else:
                sum_result[i] = sum_insede % 10
                unity_ten = unity_ten - 1
                

        else:
            sum_insede = v_value01[i] + v_value02[i]
            if(sum_insede > 9):
                unity_ten = unity_ten + 1
                sum_result[i] = sum_insede % 10
            else:
                sum_result[i] = sum_insede
    print(sum_result)
        

def multiplication():
    print("Multiplication")
    m_value01 = int(input("Please enter a string:\n"))    
    m_value02 = int(input("Please enter a string:\n"))
    m_aux = m_value01
    m = 0
    
    while m_value01 > 0:
        if m_aux == m_value01:
            value01 = m_value02
            value02 = m_value02
            value01 = str(value01)
            value02 = str(value02)
            sum_result = []
            v_value01 = []
            v_value02 = []    
            unity_ten = 0
            sum_insede = 0
            m_next = 0        
            if(len(value01) > len(value02)): #se o size da string de value01 for maior que da 2
                size = len(value01) + 1 #size recebe o size da string maior + 1
            else: #se o size da string de value02 for maior que da 1
                size = len(value02) + 1 #size recebe o size da string maior + 1        
            size = size + 1 
            while(len(value01) != size): #enquanto o size da string value01 for menor que o size
                value01 = '0' + value01 #adiciona +0 a frente da string
            while(len(value02) != size): #enquanto o size da string value01 for menor que o size
                value02 = '0' + value02 #adiciona +0 a frente da string        
            for i in range(size): #preenchendo o vetor com o size necessário para as somas
                sum_result.append(0) #todas as posições receberão         
            for i in range(size):
                m = value01[i]
                v_value01.append(int(m))   
            for i in range(size):
                m = value02[i]
                v_value02.append(int(m))           
            for i in range(size - 1, -1, -1):
                if(unity_ten > 0):
                    sum_insede = (v_value01[i] + v_value02[i]) + unity_ten
                    if(sum_insede>9):
                        sum_result[i] = sum_insede % 10
                    else:
                        sum_result[i] = sum_insede % 10
                        unity_ten = unity_ten - 1
                else:
                    sum_insede = v_value01[i] + v_value02[i]
                    if(sum_insede > 9):
                        unity_ten = unity_ten + 1
                        sum_result[i] = sum_insede % 10
                    else:
                        sum_result[i] = sum_insede
            m_value01 = m_value01 - 2
            m = 0
            for i in range(size): 
                m = str(m) + str(sum_result[i])
                m_next = int(m) 
          

           
        
        else:
            value01 = m_value02            
            value02 = str(m_next)
            value01 = str(value01)
            value02 = str(value02)
            sum_result = []
            v_value01 = []
            v_value02 = []    
            unity_ten = 0
            sum_insede = 0
            m = 0        
            if(len(value01) > len(value02)):
                size = len(value01) + 1 
            else: 
                size = len(value02) + 1      
            size = size + 1 
            while(len(value01) != size): 
                value01 = '0' + value01 
            while(len(value02) != size): 
                value02 = '0' + value02        
            for i in range(size):
                sum_result.append(0)        
            for i in range(size):
                m = value01[i]
                v_value01.append(int(m))   
            for i in range(size):
                m = value02[i]
                v_value02.append(int(m))           
            for i in range(size - 1, -1, -1):
                if(unity_ten > 0):
                    sum_insede = (v_value01[i] + v_value02[i]) + unity_ten
                    if(sum_insede>9):
                        sum_result[i] = sum_insede % 10
                    else:
                        sum_result[i] = sum_insede % 10
                        unity_ten = unity_ten - 1
                else:
                    sum_insede = v_value01[i] + v_value02[i]
                    if(sum_insede > 9):
                        unity_ten = unity_ten + 1
                        sum_result[i] = sum_insede % 10
                    else:
                        sum_result[i] = sum_insede
            m = 0
            for i in range(size): 
                m = str(m) + str(sum_result[i])
                m_next = int(m)
            m_value01 = m_value01 - 1 
    print(m_next)           
       
                
multiplication()
sum()
