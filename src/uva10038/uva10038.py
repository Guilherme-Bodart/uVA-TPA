# uva10038.py
# UVa 10038 - Jolly Jumpers

# @authors Douglas Bolis, Guilherme Bodart e Jadson Pereira.

# Get-Content entrada.txt | python uva10038.py > saida.txt  >>>>Rodando o programa com entrada por .txt

while True:
    # Até terminar as entradas
    try:
        lista = list(map(int, input().split()))
    except EOFError:
        break
    #Lista que conterá os valores para verificar o Jolly
    listaSoma = [0]*3000
    #Verifica a entrada simples : 1 2000
    if (len(lista)==2 and lista[0]==1):
        print("Jolly")
    else:
        #Coloca na listaSoma 1 em cada posicao de valor igual a sequencia para o Jolly
        for i in range(1,len(lista)-1):
            valor = abs(lista[i] - lista[i+1])
            #Condicao para adionar na Soma
            if valor < lista[0] and listaSoma[valor] == 0:
                listaSoma[valor] = 1
        i = 0
        achoum = False
        soma = 0
        #Verifica sem a sequencia tem 1, se não não é Jolly
        if(listaSoma[1]==1):
            while True and i < 3000:
                soma = soma + listaSoma[i]
                
                #Encontra o primeiro 1 depois do 0;
                if listaSoma[i]==1 and not achoum:
                    achoum = True
                #Um meio de sair do loop antes do final, caso encontre um 0 antes do tamanho final, 3000;
                if achoum:
                    if listaSoma[i]==0:
                        break
                i = i + 1
            #Verificacao do Jolly
            if soma == lista[0] - 1:
                print("Jolly")
            else:
                print("Not jolly")
        else:
            print("Not jolly")