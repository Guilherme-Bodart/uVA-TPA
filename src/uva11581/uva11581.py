# uva10107.py
# UVa 10107 - What is the Median?

# @authors Guilherme Bodart.

# Get-Content entrada.txt | python uva11581.py > saida.txt  >>>>Rodando o programa com entrada por .txt

#Verifica se a matriz esta preenchida só com zero
def tudoZero(matriz):
    for i in range(3):
        for j in range(3):
            if matriz[i][j]!=0:
                return False
    return True

#Calcula o grid de cada cedula da matriz usando seus vizinhos (soma dos vizinhos)%2
def grid(matriz):
    matrizG = [[0,0,0],[0,0,0],[0,0,0]]
    #Cada caso possivel com seus vizinhos
    matrizG[0][0] = (matriz[0][1]+matriz[1][0])%2
    matrizG[0][1] = (matriz[0][0]+matriz[1][1]+matriz[0][2])%2
    matrizG[0][2] = (matriz[0][1]+matriz[1][2])%2
    matrizG[1][0] = (matriz[0][0]+matriz[1][1]+matriz[2][0])%2
    matrizG[1][1] = (matriz[0][1]+matriz[1][0]+matriz[1][2]+matriz[2][1])%2
    matrizG[1][2] = (matriz[1][1]+matriz[0][2]+matriz[2][2])%2
    matrizG[2][0] = (matriz[1][0]+matriz[2][1])%2
    matrizG[2][1] = (matriz[2][0]+matriz[1][1]+matriz[2][2])%2
    matrizG[2][2] = (matriz[2][1]+matriz[1][2])%2

    return matrizG

def main():
    #inicia matriz
    matriz = [[0,0,0],[0,0,0],[0,0,0]]
    num = int(input())
    for n in range(num):
        for i in range(3):
            string = input()
            if(string==''): #Pula linha lida vazia
                string = input() #Pega uma string de tamanho 3
            for j in range(3):
                matriz[i][j] = int(string[j]) #Valores da matriz sendo preenchidos
                
            
        contador = -1
        #While que verifica quantas vezes a funcao grid foi usada até todos os valores ficarem 0
        while(not tudoZero(matriz)):
            matriz = grid(matriz)
            contador = contador + 1
        print(contador)
    return 0



if __name__ == "__main__":
    main()