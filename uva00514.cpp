#include<cstdio>
#include<stack>

using namespace std;

void station(int num){
  int c;
  stack<int> vagoes;
  int entrada[num];
  int saida[num];

  while(1){

    while(vagoes.size()>0){
      printf("%d\n",vagoes.top());
      vagoes.pop();
    }

    int j = 0;
    for (int i=0;i<num;i++){
      scanf("%d",&c);
      entrada[i] = c;
      if(c==0){
          return;
      }
      while(j<=num){
          if(vagoes.size()>0){
              if(vagoes.top()==c){
                  saida[i]=c;
                  vagoes.pop();
                  break;
              }
          }
          if(c==j+1){
              saida[i]=c;
              j = j + 1;
              break;
          }
          else{
              vagoes.push(j+1);
          }
          j = j + 1;
      }
      
    }
    for(int q=0;q<num;q++){
        printf("%d:",num);
        printf("%d\n",saida[q]);
    }

  }

}

int main() {

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