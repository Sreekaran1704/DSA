//Question code : SECLAR
#include <bits/stdc++.h>
using namespace std;


int main() {
	// your code goes here
	int array[3];
	for(int i=0;i<3;i++){
	    cin>>array[i];
	}int n=sizeof(array)/sizeof(array[0]);
	sort(array,array+n);
	for(int i=0;i<3;i++){
	    if(i==1){
	        cout<<array[i];
	    }
	}
	return 0;
}
