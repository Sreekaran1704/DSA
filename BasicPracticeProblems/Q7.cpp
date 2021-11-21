//Question code : :REVMEE
#include <algorithm>
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int n;
	cin>>n;
	int array[n];
	for(int i=0;i<n;i++){
	    cin>>array[i];
	    
	}int a=sizeof(array)/sizeof(array[0]);
	reverse(array,array+n);
	for(int i=0;i<n;i++ ){
	    cout<<array[i]<<" ";
	}
	return 0;
}
