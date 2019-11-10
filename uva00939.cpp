#include <iostream>
#include<cstdio>
#include <map>

using namespace std;

bool existe(const string& nome, const map<string, string*>& pessoas){
    auto res = pessoas.find(nome);
    if (res != pessoas.end())
        return true;
    else
        return false;
}
int main() {
    map<string, string*> mapa;
    int num;
    cin>>num;
    printf("%d\n",num);
    
    for (int i=0; i<num; i++){
        string primeiro;
        string segundo;
        cin>>primeiro;
        cin>>segundo;

        if(!existe(primeiro,mapa)){
            string vetor[5];
            mapa[primeiro] = vetor;
        }
        if(segundo=="dominant" or segundo=="recessive" or segundo=="non-existent"){
            mapa[primeiro][0] = segundo;
        }
        else{
            mapa[primeiro][1] = segundo;        
            if(!existe(segundo,mapa)){
                string vetor2[5];
                mapa[segundo] = vetor2;
            }
            if(mapa[segundo][1]==""){
                mapa[segundo][1]=primeiro;
            }
            else{
                mapa[segundo][2]=primeiro;
            }
        }
    
    }
  map<string, string*>::iterator it;
  for(it = mapa.begin(); it != mapa.end(); ++it)
		printf("%s %s\n",it->first.c_str(),it->second[0].c_str());
}