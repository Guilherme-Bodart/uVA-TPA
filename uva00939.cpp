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
    string vetor[5];
    string primeiro;
    string segundo;
    cin>>primeiro;
    cin>>segundo;

    mapa[primeiro] = vetor;
    if(segundo=="dominant" or segundo=="recessive" or segundo=="existent"){
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
  printf("%s\n",mapa[segundo][2].c_str());
}