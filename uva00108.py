def main():
    while True:
        listaSoma = []
        listaTemp = []       
        soma = 0
        maxSoma = -1000
        try:
            dim = int(input())
        except EOFError:
            break
        while True:
            try:
                listaTemp += map(int,input().split())
            except:
                break
        f = 0
        g = 0
        listaSoma.append([])
        for x in listaTemp:
            listaSoma[g].append(x)
            f = f + 1
            if f==dim:
                f=0
                g+=1
                if(g<dim):
                    listaSoma.append([])

        for n in range(dim):
            for m in range(dim):
                if n > 0:
                    listaSoma[n][m] = listaSoma[n][m] + listaSoma[n-1][m]                
                if m > 0:
                    listaSoma[n][m] = listaSoma[n][m] + listaSoma[n][m-1]               
                if n > 0 and m > 0:
                    listaSoma[n][m] = listaSoma[n][m] - listaSoma[n-1][m-1]               

        for i in range(dim):            
            for j in range(dim):
                for lin in range(i,dim):
                    for col in range(j,dim):
                        soma = listaSoma[lin][col]                    
                        if i > 0:
                            soma = soma - listaSoma[i-1][col] 
                
                        if j > 0:
                            soma = soma - listaSoma[lin][j-1] 
                        
                        if i > 0 and j > 0:
                            soma = soma + listaSoma[i-1][j-1] 

                        if soma > maxSoma:
                            maxSoma = soma
        print(maxSoma)
    return 0



if __name__ == "__main__":
    main()