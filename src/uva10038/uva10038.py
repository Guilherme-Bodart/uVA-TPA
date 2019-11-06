while True:
    try:
        lista = list(map(int, input().split()))
    except EOFError:
        break
    listaSoma = [0]*3000
    if (len(lista)==2 and lista[0]==1):
        print("Jolly")
    else:
        for i in range(1,len(lista)-1):
            valor = abs(lista[i] - lista[i+1])
            if valor < lista[0] and listaSoma[valor] == 0:
                listaSoma[valor] = 1
        i = 0
        achoum = False
        soma = 0
        if(listaSoma[1]==1):
            while True and i < 3000:
                soma = soma + listaSoma[i]
                
                if listaSoma[i]==1 and not achoum:
                    achoum = True
                if achoum:
                    if listaSoma[i]==0:
                        break
                i = i + 1
            if soma == lista[0] - 1:
                print("Jolly")
            else:
                print("Not jolly")
        else:
            print("Not jolly")