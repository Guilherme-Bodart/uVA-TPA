#include<cstdio>
#include<stack>

using namespace std;

void station(int num){
  int numVagao;
  stack<int> vagoes;
  int entrada[num];
  int saida[num];

  while(1){
      //Caso tenha algo na pilha
      while(vagoes.size()>0){      
          vagoes.pop();
      }

      int j = 0;
      for (int i=0;i<num;i++){
          scanf("%d",&numVagao);
          entrada[i] = numVagao;
          //Se colocar 0, volta a perguntar o tamanho do "trem"
          if(numVagao==0){
              return;
          }

          while(j<=num){
              //Verifica se a pilha nao esta vazia e se o topo dela é igual a entrada
              if(vagoes.size()>0 && vagoes.top()==numVagao){
                  break;                    
              }
              //Da push          
              vagoes.push(j+1);
              j = j + 1;
          }
          //Tira da pilha e coloca na lista de saida
          if(vagoes.top()==numVagao){
              saida[i] = numVagao;
              vagoes.pop();
          }        
      }
      //Compara lista saida com a lista de entrada
      int verif = 0;
      for(int q=0;q<num;q++){

          if(!(saida[q]==entrada[q])){
              verif = 0;
              break;
          }
          else{
              verif=1;
          }        
      }

      if (verif){
          printf("Yes\n");
      }
      else{
          printf("No\n");
      }
    }
}

int main() {
  //Le ate ser 0 e para quando zerar
  while(1){
    int num;
    scanf("%d",&num);
    if(num==0){
        break;
    }
    station(num);
    printf("\n");
  }

}