#include <iostream>
#include <array>
#include <math.h>
using namespace std;

bool isPrime(int n){
    if(n == 2){
        return true;
    }
    if(n<2 || n%2 == 0){
        return false;
    }
    for(int i =3; i<((int) sqrt(n))+1;i+=2){
        if (n%i==0){
            return false;
        }
    }
    return true;
}

int getNUmberOfPrimes(int n){
    int cont = 0;
    for(int i =0;i<n;i++){
        if(isPrime(i) == true){
            cont+=1;
        }
    }
    return cont;
}


int main(){
    int aux = getNUmberOfPrimes(4000000);
    cout<<aux;
}


