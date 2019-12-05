def main(): 
    first=True
    while int(input())!=0:
        if(first):
            first=False
        else:
            print()
        lista = list(map(int, input().split()))
        lista.sort()
        qtdRepetidasMax = 1
        qtdRepetidas = 1

        for i in range(len(lista)-1):
            if lista[i]==lista[i+1]:
                qtdRepetidas += 1
            else:
                if qtdRepetidas>=qtdRepetidasMax:
                    qtdRepetidasMax = qtdRepetidas
                qtdRepetidas = 1
        if qtdRepetidas>=qtdRepetidasMax:
            qtdRepetidasMax = qtdRepetidas

        mochilas = []
        for i in range(qtdRepetidasMax):
            mochilas.append([])
        i = 0

        for j in range(len(lista)):
            mochilas[i].append(lista[j])
            i = i + 1
            if(i>=qtdRepetidasMax):
                i=0
        print(len(mochilas))
        for i in range(len(mochilas)):
            for j in range(len(mochilas[i])):
                if j<len(mochilas[i])-1:
                    print(mochilas[i][j],"",end="")
                else:
                    print(mochilas[i][j],end="")
            print()
        
    return 0



if __name__ == "__main__":
    main()