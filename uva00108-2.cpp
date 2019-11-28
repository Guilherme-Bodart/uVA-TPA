// UVa 00514 - Rails

// @authors Guilherme Bodart.

#include<cstdio>
#include<stack>
using namespace std;

int main() {
  while (1){
        int listaSoma[100][100];
        int soma = 0;
        int maxSoma = -1000;
        int dim;
        scanf("%d",&dim);
        
        for(int n=0;n<dim;n++){
            for(int m=0;m<dim;m++){
              scanf("%d",&listaSoma[n][m]);
            }
        }
        for(int i=0;i<dim;i++){         
            for(int j=0;j<dim;j++){
                for(int lin=0;lin<i+1;lin++){
                    for(int col=0;col<j+1;col++){
                        soma = 0;
                        for (int k=lin;k<i+1;k++){
                            for(int q=col;q<j+1;q++){
                                try{
                                    soma = soma + listaSoma[k][q];
                                }   
                                catch(int erro){
                                    soma = soma;
                                }
                            }
                        }
                        if(soma>maxSoma){
                            maxSoma = soma;
                        }
                    }
                }
            }
        }
        printf("%d",maxSoma);
    return 0;
  }
}