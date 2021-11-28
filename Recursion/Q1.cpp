#include <bits/stdc++.h>
using namespace std;

void pattern(int n){
    if(n==0){
        return ;
    }
    pattern(n-1);
    for(int i=1;i<=n;i++){
        cout<<i<<" ";
    }cout<<"\n";
}

int main(){
    int a;
    cin>>a;
    pattern(a);
}