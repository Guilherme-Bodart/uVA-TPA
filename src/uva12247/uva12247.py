
'''
	Jadson Pereira
	uva12247 - jollo
'''

#Leitura dos dados do arquivo.
def entrada():
    return input()
    
cartas = entrada()
avaliable = [True] * 53 # lst[53] cartas disponiveis
flag = 0		# Verifica se ja passou na função.
answer = 100
while(cartas != "0 0 0 0 0"):
    lstCartas = cartas.split(" ")
    princess = lstCartas[:3]
    prince = lstCartas[3:]
    #transforma para inteiro.
    princess = [
        int(lstCartas[0]),
        int(lstCartas[1]),
        int(lstCartas[2])
    ]

    prince = [
        int(lstCartas[3]),
        int(lstCartas[4])
    ]
    #Ordenando as listas para a comparação.
    princess.sort()
    prince.sort()
    #desabilita as cartas na mão.
    avaliable[princess[0]] = False
    avaliable[princess[1]] = False
    avaliable[princess[2]] = False
    avaliable[prince[0]] = False
    avaliable[prince[1]] = False
    #As duas cartas do principe são maiores.
    if(prince[0]>princess[2] and flag == 0):
        #Qualquer carta satisfaz.
        for i in range (1,len(avaliable)):
            if(avaliable[i]):
                answer = i
                flag = 1
                break
        #print(answer)
        
    #Se uma carta do principe é maior que todas da princesa.
    if(prince[1] > princess[2] and flag == 0):
        i=princess[2] +1
        while(i<53):
            if(avaliable[i]):
                answer = i
                break
            i += 1
    	#caso a carta esteja indisponivel
	#caso do [4 50 51 10 52]
        if(i>52):
            answer = -1
        

    #se as duas cartas forem menor que só 1 carta dela..
    if(prince[0]>princess[1] and flag == 0):
        i=(princess[1]) + 1
        while(i<53):
            if(avaliable[i]):
                answer = i
                break
            i += 1  
    #As duas cartas do principe são menores.
    #Ou a maior carta da princesa for maior que 52.
    if(prince[0]<princess[1] and prince[1] < princess[2] and flag == 0) :
        #Não tem como ganhar.  
        answer = -1
        avaliable[princess[2]] = False


    avaliable[answer] = False
    print(answer)     
    #reseta a lista
    flag = 0
    avaliable = [True] * 53
    cartas = entrada()
