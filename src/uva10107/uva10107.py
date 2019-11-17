# uva10107.py
# UVa 10107 - What is the Median?

# @authors Guilherme Bodart.

# Get-Content entrada.txt | python uva10107.py > saida.txt  >>>>Rodando o programa com entrada por .txt


lista = []
while True:
    # Até terminar as entradas
    try:
        num = int(input())
    except EOFError:
        break

    lista.append(num)
    #Ordena lista
    lista.sort()
    #Tamanho Ímpar
    if(len(lista)%2==1):
        print(lista[len(lista)//2])
    #Tamanho Par
    else:
        print(((lista[(len(lista)//2)-1] + lista[len(lista)//2]))//2)
