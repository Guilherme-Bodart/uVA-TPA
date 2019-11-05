int matriz[3][3];

int tudoZero(){
    for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
            if(matriz[i][j]!=0){
                return 0;
            }
        }
    }
    return 1;

}

void grid(int matriz[3][3]){
    int matrizG[3][3];
    matrizG[0][0] = (matriz[0][1]+matriz[1][0])%2;
    matrizG[0][1] = (matriz[0][0]+matriz[1][1]+matriz[0][2])%2;
    matrizG[0][2] = (matriz[0][1]+matriz[1][2])%2;

    matrizG[1][0] = (matriz[0][0]+matriz[1][1]+matriz[2][0])%2;
    matrizG[1][1] = (matriz[0][1]+matriz[1][0]+matriz[1][2]+matriz[2][1])%2;
    matrizG[1][2] = (matriz[1][1]+matriz[0][2]+matriz[2][2])%2;

    matrizG[2][0] = (matriz[1][0]+matriz[2][1])%2;
    matrizG[2][1] = (matriz[2][0]+matriz[1][1]+matriz[2][2])%2;
    matrizG[2][2] = (matriz[2][1]+matriz[1][2])%2;
    
    for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
            matriz[i][j] = matrizG[i][j];
        }
    } 


}


int main(){
    
    int num = scanf("%d",&num);

    for(int n=0;n<num;n++){
        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                scanf("%1d", &matriz[i][j]);
            }
        }
        int contador = -1;
        int verif;
        while(!tudoZero()){
            grid(matriz);
            contador = contador + 1;
        }
        printf("%d",contador);
    }
}