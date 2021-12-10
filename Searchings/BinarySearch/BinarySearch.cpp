#include <bits/stdc++.h>
using namespace std;

void binarySearch(int arr[],int n,int high,int low){
    int mid = (high+low)/2;
    if(arr[mid] == n){
        cout<<"Element found at index "<<mid<<endl;
        return;
    }
    else if(arr[mid] > n){
        binarySearch(arr,n,mid-1,low);
    }
    else{
        binarySearch(arr,n,high,mid+1);
    }
}

int main(){
    int array[]={1,2,3,4,5,6,7,8,9,10};
    cout<<"Enter the number to be searched:";
    int n;
    cin>>n;
    binarySearch(array,n,9,4);
}