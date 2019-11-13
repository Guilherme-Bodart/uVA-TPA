while(True):
    n,m = input().split()
    n = int(n)
    m = int(m)
    if(n==0 and m==0):
        break
    lista = [0]*1000000  
    conflite = False
    for q in range(n):
        inicio,final = input().split()
        inicio = int(inicio)
        final = int(final)
        for i in range(inicio,final):
            if lista[i]==0:
                lista[i] = 1
            else:
                conflite = True
                break

    for k in range(m):
        inicio,final,repeticao = input().split()
        inicio = int(inicio)
        final = int(final)
        repeticao = int(repeticao)
        j = 0
        while(not conflite and inicio < 1000000):
            for j in range(inicio,final):
                if lista[j]==0:
                    lista[j] = 1
                else:
                    conflite = True
                    break
            inicio = inicio + repeticao
            final = min(final + repeticao,1000000)    
    if(conflite):
        print("CONFLICT")
    else:
        print("NO CONFLICT")