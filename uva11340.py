testeNum = int(input(""))
i = 0

while (i < testeNum):

    listaLetra = []
    listaValor = []
    listaQuant = []
    j=0
    k=0
    valorTotal = 0
    frase = ""

    quantidadeValores = int(input(""))    
    while(j < quantidadeValores):
        valores = input("").split()
        listaLetra.append(valores[0])
        listaValor.append(int(valores[1]))
        j = j + 1

    quantidadeLinhas = int(input(""))    
    while(k < quantidadeLinhas):
        linha = input("")
        frase = frase + " " + linha
        k = k + 1
    
    for r in range(0,len(listaLetra)):
        quantidadeLetra = frase.count(listaLetra[r])
        valorTotal = valorTotal + (listaValor[r] * quantidadeLetra)

    i = i + 1
    print("%.2f$"%(valorTotal/100))
    

