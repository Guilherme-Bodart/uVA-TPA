
def maxIndex(lst:list):
    maxInd = 0
    value = lst[0]
    for i in range(len(lst)):
        if (value<lst[i]):
            value = lst[i]
            maxInd = i
    return maxInd


def main():
    answer = 0
    usedCards = []
    cartas = input('Entre com as 5 cartas: \n')
    cartas = cartas.split(" ")
    while (cartas != ['0','0','0','0','0']):
        princess = cartas[:3]
        prince = cartas[3:]
        #pega o maior index de cada lista.
        maxPrince = maxIndex(prince)
        maxPrincess = maxIndex(princess)
        #caso1: Carta do Principe serem maior que a da princesa.
        if(prince[0]>princess[0] and prince[1]>princess[1]):
            #se a ultima carta da princesa for maior que as 2 do principe. 
            if(princess[2] > prince[0] and princess[2] > prince[1]):
                if(princess[2] in usedCards):
                    answer = int(princess[1]) + 1
                else:
                    answer = int(princess[2]) +1
            else:
                ans = int(princess[2]) +1
                if(str(ans) not in usedCards):
                    answer = ans                
                else:
                    if(int(prince[maxPrince]) == ans):
                        answer = ans+1
            usedCards.append(str(answer))   
        #caso3: Se as cartas da princesa forem maiores
        if(prince[maxPrince]<princess[maxPrincess]):
            if (princess[maxPrincess] not in usedCards):
                usedCards.append(princess[maxPrincess])
                answer = -1
        print(answer)  
        print(usedCards)
        cartas = input('Entre com as 5 cartas:\n')
        cartas = cartas.split(" ")
        

main()