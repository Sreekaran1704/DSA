//QuestionCode : DIFACTRS
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int n,count=0;
	cin>>n;
	
	for(int i=1;i<=n;i++){
	    if(n%i==0){
	        count+=1;
	    }
	}cout<<count<<"\n";
	for(int i=1;i<=n;i++){
	    if(n%i==0){
	        cout<<i<<" ";
	    }
	}
	return 0;
}
