def arvoreGenetica(mapa):
    tam = 0
    for j in mapa:

        if (mapa[j][0]==""):
            verifGenetica(j,mapa)
    return mapa


def verifGenetica(pessoa,mapa):
    primeiro = "";
    segundo = "";
    if mapa[pessoa][2] in mapa:
        primeiro = mapa[pessoa][2]
    if mapa[pessoa][3] in mapa:
        segundo = mapa[pessoa][3]
    if(mapa[primeiro][0] == ""):
        verifGenetica(primeiro)
    if(mapa[segundo][0] == ""):
        verifGenetica(segundo) 
    if (mapa[segundo][0] == "non-existent"):
        mapa[pessoa][0] = "non-existent"
    elif (mapa[primeiro][0] == "non-existent"):
        mapa[pessoa][0] = "non-existent"
    elif (mapa[primeiro][0] == "dominant" and mapa[segundo][0] == "recessive"):
        mapa[pessoa][0] = "dominant" 
    elif (mapa[primeiro][0] == "recessive" and mapa[segundo][0] == "dominant"):
        mapa[pessoa][0] = "dominant"
    elif (mapa[primeiro][0] == "recessive" and mapa[segundo][0] == "recessive"):
        mapa[pessoa][0] = "recessive"
    return mapa

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
        if (segundo=="dominant" or segundo=="recessive" or segundo=="non-existent") :
            mapa[primeiro][0] = segundo
        else:
            mapa[primeiro][1] = segundo
            if (not segundo in mapa):
                mapa[segundo] = lista2;
                listaOrd.append(segundo)
            if (mapa[segundo][2]==""):
                mapa[segundo][2]=primeiro
            else:
                mapa[segundo][3]=primeiro
    
    mapa = arvoreGenetica(mapa)
    
    listaOrd.sort()
    for j in range(len(listaOrd)):
        print(listaOrd[j],mapa[listaOrd[j]][0])
 

    return 0



if __name__ == "__main__":
    main()