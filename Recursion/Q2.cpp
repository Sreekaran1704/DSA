#include <bits/stdc++.h>
using namespace std;

void pattern2(int n){
    if(n==0){
        return;
    }
      for(int i=1;i<=n;i++){
          cout<<i<<" ";
      }cout<<"\n";
    pattern2(n-1);
    for(int i=1;i<=n;i++){
          cout<<i<<" ";
}cout<<"\n";
}

int main(){
pattern2(4);

}