# uva01062.py
# UVa 01062 - Containers

# @authors Jadson Pereira.

# Get-Content entrada.txt | python uva01062.py > saida.txt  >>>>Rodando o programa com entrada por .txt


#Leitura dos dados do arquivo.
def entrada():
    return input()
#inicio da solução
indexCase: int = 1
data = entrada()
while(data != 'end'):
    stackContainers:list = []
    if(data != ' '):
        #Percorrer a linha.
        for i in range(0,len(data)):
            currentContainer = data[i]
            if(currentContainer != '\n'):
                #Procura o container.
                j:int = 0
                while(j<len(stackContainers)):
                    if(currentContainer <= stackContainers[j][-1]):
                        stackContainers[j].append(currentContainer)
                        break
                    j +=1
                #endwhile
                #Não achou o container.
                if(j == len(stackContainers)):
                    stack = [currentContainer]
                    stackContainers.append(stack)
        #endfor
    #print(stackContainers) 
    print("Case "+str(indexCase)+ ": "+str(len(stackContainers)))
    indexCase = indexCase + 1
    data = entrada()
#endwhile

