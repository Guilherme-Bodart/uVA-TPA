// uva00978.py
// UVa 00978 - Lemmings Battle!

// @authors Guilherme Bodart.

#include<cstdio>
#include <iostream>
#include<set>
using namespace std;

int main(){
    multiset<int, greater<int> > eVerde,eAzul,armVerde,armAzul;
    int batalhas;
    scanf("%d",&batalhas);
    for(int i=0;i<batalhas;i++){
        eVerde.clear();eAzul.clear();
        int CB,EV,EA,valor;
        scanf("%d",&CB);scanf("%d",&EV);scanf("%d",&EA);
        for(int v=0;v<EV;v++){
            scanf("%d",&valor);
            eVerde.insert(valor);
        }
        for(int a=0;a<EA;a++){
            scanf("%d",&valor);
            eAzul.insert(valor);
        }

        multiset<int, greater<int> >::iterator lemmingV,lemmingA;
        while(eVerde.size() && eAzul.size()){ 
            armVerde.clear(); armAzul.clear();

            for(int b=0;b<CB;b++){
                if(!eAzul.empty() && !eVerde.empty()){
                    lemmingA = eAzul.begin();
                    lemmingV = eVerde.begin();
                    if(*lemmingA>*lemmingV){
                        armAzul.insert(*lemmingA-*lemmingV);
                    }
                    else{
                        if(*lemmingA<*lemmingV){
                            armVerde.insert(*lemmingV-*lemmingA);
                        }
                    }
                    eVerde.erase(lemmingV);eAzul.erase(lemmingA);
                }
                else{
                    break;
                }      
            }

            for (lemmingV = armVerde.begin(); lemmingV != armVerde.end(); ++lemmingV){
                eVerde.insert(*lemmingV);    
            }

            for (lemmingA = armAzul.begin(); lemmingA != armAzul.end(); ++lemmingA){
                eAzul.insert(*lemmingA);    
            }
        }
        
        if(eVerde.empty() && eAzul.empty()){
            printf("green and blue died\n");
        }
        else{
            if(eVerde.empty()){
                printf("blue wins\n");
                for (lemmingA = eAzul.begin(); lemmingA != eAzul.end(); ++lemmingA){
                    cout << *lemmingA << "\n";
                }
            }
            else{
                printf("green wins\n");
                for (lemmingV = eVerde.begin(); lemmingV != eVerde.end(); ++lemmingV){
                    cout << *lemmingV << "\n";
                }
            }
        }
        if(i<batalhas-1){ 
            printf("\n");
        }
    }

};