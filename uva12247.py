#Leitura dos dados do arquivo.
def entrada():
    return input()
#Lista de cartas disponiveis
def avaliable():
    avaliable = []
    for i in range(53):
        avaliable.append(True)
    return avaliable 

cartas = entrada()
avaliable = avaliable()
answer = 53
while(cartas != "0 0 0 0 0"):
    lstCartas = cartas.split(" ")
    princess = lstCartas[:3]
    prince = lstCartas[3:]
    
    #As duas cartas do principe são maiores.
    if(prince[0]>princess[0] and prince[1] > princess[1]):
        #Qualquer carta satisfaz.
        for i in range (len(avaliable)):
            if(avaliable[i]):
                answer = i
                break
        
    #As duas cartas do principe são menores.
    if(prince[0]<princess[0] and prince[1] < princess[1]):
        #Não tem como ganhar.
        anser = -1

    #Se uma carta é maior.
    if()

    cartas = entrada()