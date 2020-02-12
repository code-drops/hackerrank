/*
https://www.hackerrank.com/challenges/30-2d-arrays/problem

Given a  2D Array,
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:

a b c
  d
e f g

There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values.
Task : Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

*/

#include <iostream>
using namespace std;
int a[6][6];
int func(int r,int c,int max){
    int s=0;
    for(int i=r;i<=r+2;i++){
        for(int j=c;j<=c+2;j++){
            if(((i==r+1)&&(j==c))||((i==r+1)&&(j==c+2))){
                continue;
            }
            s = s + a[i][j];
        }
    }
    if(max<s){
        max = s;
    }
    return max;
}
int main()
{
    int max = 0;
    for(int i=0;i<6;i++){
        for(int j=0;j<6;j++){
            cout << "a["<<i<<"]["<<j<<"] : ";
            cin >> a[i][j];
        }
    }
    for(int i=0;i<=3;i++){
        for(int j=0;j<=3;j++){
            max = func(i,j,max);
        }
    }
    cout << <"max : "<< max;
    return 0;
}
