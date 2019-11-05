def tudoZero(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]!=0:
                return False
    return True


def grid(matriz):
    matrizG = [[0,0,0],[0,0,0],[0,0,0]]
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
    matriz = [[0,0,0],[0,0,0],[0,0,0]]
    num = int(input())
    for n in range(num):
        for i in range(3):
            string = input()
            for j in range(3):
                matriz[i][j] = int(string[j])
        contador = -1
        while(not tudoZero(matriz)):
            matriz = grid(matriz)
            contador = contador + 1
        print(contador)
    return 0



if __name__ == "__main__":
    main()