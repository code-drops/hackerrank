'''
You have to complete the function void update(int *a,int *b), which reads two integers as argument, and sets a  with the sum of them, and b with the absolute difference of them.
'''
#include<iostream>
#include<stdio.h>
#include<cmath>
using namespace std;
void update(int *a,int *b) {
    int temp = *a;
    *a = *a + *b;
    *b = abs(temp - *b);
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;

    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
