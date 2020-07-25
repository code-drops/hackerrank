'''
Consider an n-element array,a , where each index i in the array contains a reference to an array of ki integers (where the value of ki varies from array to array). See the Explanation section below for a diagram.

Given ,a you must answer q queries. Each query is in the format i j, where i denotes an index in array a and j denotes an index in the array located at a[i] . For each query, find and print the value of element j in the array at location a[i]  on a new line.
'''

#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
int n,q;
cin>>n>>q;
int** seq=new int* [n];
for(int i=0;i<n;i++)
    {
      int a;
      cin>>a;
      int* b=new int [a];
      for(int j=0;j<a;j++)
        {
          int e;
          cin>>e;
          b[j]=e;
        }
    *(seq+i)=b;
   }

  for(int i=0;i<q;i++)
  {
  int r,s;
  cin>>r>>s;
  cout<<seq[r][s]<<endl;
  }
}
