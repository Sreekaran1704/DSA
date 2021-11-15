#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,m;
    cin>>n>>m;

    //adjacent matrix
    int a[n+1][n+1];

    //take edges as input
    for(int i=0;i<m;i++){
        int u,v;
        cin>>u>>v;
        a[u][v]=1;
        a[v][u]=1;
    }
    return 0;
}