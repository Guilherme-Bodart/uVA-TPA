indexCase: int = 1

def entrada():
    return input()
   
data = entrada()
while(data != 'end'):
    stackContainers:list = []
    #print(data)
    if(data != ' '):
        #Percorrer a linha.
        for i in range(0,len(data)):
            currentLetter = data[i]
            if(currentLetter != '\n'):
                #Procura o container.
                j:int = 0
                while(j<len(stackContainers)):
                    if(currentLetter <= stackContainers[j][-1]):
                        stackContainers[j].append(currentLetter)
                        break
                    j +=1
                #endwhile
                #Não achou.
                if(j == len(stackContainers)):
                    stack = [currentLetter]
                    stackContainers.append(stack)
        #endfor
    #print(stackContainers) 
    print("Case "+str(indexCase)+ ": "+str(len(stackContainers)))
    indexCase = indexCase + 1
    data = entrada()
#endwhile

