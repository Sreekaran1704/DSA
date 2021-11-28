#include <bits/stdc++.h>
using namespace std;

void say_hello(int n){
    if(n==0){
        return;
    }
    cout<<"hello"<<endl;
    say_hello(n-1);
}

int main(){
say_hello(2);
}