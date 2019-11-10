def genetica(mapa,listaOrd):
    tam = 0
    for j in mapa:

        
        if (mapa[j][0]==""):

            if (mapa[primeiro][0] or mapa[segundo][0]):
                print('x')

        
        if mapa[j][2] in mapa:
            primeiro = mapa[j][2]
        segundo = mapa[j][3]

        

    return 0


def main():

    mapa = {}
    num = int(input())
    listaOrd = []
    for i in range(num):
        lista = ["","","","",""]
        lista2 = ["","","","",""]
        string = input().split()
        primeiro = string[0];
        segundo = string[1];
        if (not primeiro in mapa):
            mapa[primeiro] = lista
            listaOrd.append(primeiro)
            print(listaOrd)
        if (segundo=="dominant" or segundo=="recessive" or segundo=="non-existent") :
            mapa[primeiro][0] = segundo
        else:
            mapa[primeiro][1] = segundo
            if (not segundo in mapa):
                mapa[segundo] = lista2;
                listaOrd.append(segundo)
                print(listaOrd)
            if (mapa[segundo][2]==""):
                mapa[segundo][2]=primeiro
            else:
                mapa[segundo][3]=primeiro
    
    #mapa = genetica(mapa,listaOrd)
    
    listaOrd.sort()
    for j in (mapa):
        print(j,mapa[j])
 

    return 0



if __name__ == "__main__":
    main()