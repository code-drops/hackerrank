//Write a program to find whether a no is power of two.


#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include<cmath>
#include <algorithm>
using namespace std;
int main()
{
    long int a;
    cin >> a;
    if(ceil(log2(a))==floor(log2(a)))
    {
        cout << "Yes";
    }
    else{
        cout << "No";
    }
    return 0;
}
