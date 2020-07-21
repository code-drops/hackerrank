// Task is as follows - Vikas Bhayia gives Q queries each query containing two integers a and b. Your task is to count the no of set-bits in for all numbers between a and b (both inclusive)
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

unsigned int sum(unsigned int n)
{
    int count = 0;
    while (n) {
        count += n & 1;
        n >>= 1;
    }
    return count;
}

int main()
{
    int a,b,n,s;
    cin >> n;
    for(int i=0;i<n;i++)
    {
        s = 0;
        cin >> a >> b;
        for(int j=a;j<=b;j++)
        {
            s += sum(j);
        }
        cout << s << endl;
    }
    return 0;
}
