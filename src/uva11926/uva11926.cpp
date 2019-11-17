// uva11926.py
// UVa 11926 - Multitasking

// @authors Guilherme Bodart.

#include<cstdio>
#include<bitset>
using namespace std;


int main(){
    while(true){        
        int n,m;
        scanf("%d",&n);
        scanf("%d",&m);
        if(n==0 && m==0){
            break;
        }
        bitset<1000005> listaBit;
        bool conflite = false;

        for(int q=0;q<n;q++){
            int inicio,fim;
            scanf("%d",&inicio);
            scanf("%d",&fim);
            for(int i=inicio;i<fim;i++){
                if(!listaBit.test(i)){
                    listaBit.set(i);
                }
                else{
                    conflite=true;
                    break;
                }
            }
        }
        for(int k=0;k<m;k++){
            int inicio,fim,repeticao;
            scanf("%d",&inicio);
            scanf("%d",&fim);
            scanf("%d",&repeticao);
            while(!conflite and inicio < 1000000){
                for(int j=inicio;j<fim;j++){
                    if(!listaBit.test(j)){
                        listaBit.set(j);
                    }
                    else{
                        conflite = true;
                        break;
                    }
                }
                inicio = inicio + repeticao;
                fim = min(fim + repeticao,1000000);
            }
        }
        if(conflite){
            printf("CONFLICT\n");
        }
        else{
            printf("NO CONFLICT\n");
        }
    }

}