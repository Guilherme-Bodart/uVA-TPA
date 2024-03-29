# uva10264.py
# UVa 10264 - The Most Potent Corner

# @authors Guilherme Bodart.

# Get-Content entrada.txt | python uva10264.py > saida.txt  >>>>Rodando o programa com entrada por .txt



while(True):
    try:
        num = int(input())
    except EOFError:
        break
    cubo,cuboSoma = {},{}
    listaVizinhos = []
    for i in range((2**num)):
        try:
            peso = int(input())
        except EOFError:
            break
        numB = bin(i)[2:]        
        chave = str(0)*(num-len(numB)) + numB
        cubo[chave] = peso
    for key in cubo:    
        soma = 0
        for k in range(num):
            if(key[k])=='0':
                string = key[0:k]+ '1' + key[k+1:]
                if string in cubo:
                    soma = soma + cubo[string]
                    listaVizinhos.append(string)
            else:
                string = key[0:k]+ '0' + key[k+1:]
                if string in cubo:
                    soma = soma + cubo[string]
                    listaVizinhos.append(string)
        cuboSoma[key] = soma
    maior,y = 0,0
    for s in cuboSoma:        
        for e in range(num):
            try:
                soma = cuboSoma[s] + cuboSoma[str(listaVizinhos[(y*num + e)])]
            except:
                soma = cuboSoma[s]            
            if(soma>maior):
                maior = soma      
        y = y + 1 
    print(maior)