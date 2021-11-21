//Question code : FINDMELI
#include <bits/stdc++.h>
using namespace std;
 
int main()
{
 
    int n, x, i, k;
    cin >> n >> k;
 
    set<int> s;
    for (i = 0; i < n; i++)
    {
        cin >> x;
        s.insert(x);
    }
 
    if (s.find(k) == s.end())
        cout << -1 << endl;
    else
        cout << 1 << endl;
}
 