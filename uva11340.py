def main():
    testNum = int(input())
    i = 0

    listValue = [0]*260

    while (i < testNum and i < 5):
    #for i in range(testNum):

        listChar = []    
        j = 0
        k = 0
        valueTotal = 0
        listAmout = [0]*260

        amoutValues = int(input())    
        while(j < amoutValues and j < 100):
        #for j in range(amoutvalues):
            values = input()
            listChar.append(values[0])
            listValue[ord(values[0])] = (int(values[2:]))
            j = j + 1
        amoutLines = int(input())    
        while(k < amoutLines and k < 150000):
        #for k in range(amoutLines):
            line = input()[0:10000]
            for r in range(0,len(line)):
                listAmout[ord(line[r])] = listAmout[ord(line[r])] + 1
            k = k + 1
        
        for w in (listChar):
            valueTotal = valueTotal + (listAmout[ord(w)]*listValue[ord(w)])

        print("%.2f$"%(valueTotal/100))
        i = i + 1
        
if __name__ == "__main__":
    main()