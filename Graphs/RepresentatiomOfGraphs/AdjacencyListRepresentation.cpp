#include <bits/stdc++.h>
using namespace std;
int main(){
    int m,n;
    cin>>n>>m;

    vector<int>adj[n+1];
    for(int i=0;i<m;i++){
        int u,v;
        cin>>v>>u;

        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    return 0;
}