while(True):
    try:
        num = int(input())
    except EOFError:
        break
    cubo = {}
    cuboSoma = {}
    listaVizinhos = []
    for i in range((num*num)-1):
        peso = int(input())
        numB = bin(i)[2:]
        chave = str(0)*(num-len(numB)) + numB
        cubo[chave] = peso;

    for key in cubo:    
        soma = 0
        for k in range(num):
            if(key[k])=='0':
                string = key[0:k]+ '1' + key[k+1:]
                soma = soma + cubo[string]
            else:
                string = key[0:k]+ '0' + key[k+1:]
                soma = soma + cubo[string]                
            listaVizinhos.append(string)

        cuboSoma[key] = soma
    print(listaVizinhos)
    for s in cuboSoma:
        print(s,cuboSoma[s])
    maior = 0
    y = 0
    for s in cuboSoma:        
        for e in range(num):
            soma = cuboSoma[s] + cuboSoma[str(listaVizinhos[(y*num + e)])]
            if(soma>maior):
                maior = soma      
        y = y + 1 
    print(maior)