'''
Given a 6*6 2D Array, arr:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
We define an hourglass in A to be a subset of values with indices falling in this pattern in arr's graphical representation:

a b c
  d
e f g
There are 16 hourglasses in arr, and an hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum.
'''

import sys
def hourglassSum(a):
    n = len(a)
    max = -sys.maxsize
    for i in range(0,n-2):
        # print(i)
        for j in range(0,n-2):
            s = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+1] + a[i+2][j] + a[i+2][j+1] + a[i+2][j+2]
            if max<s:
                max = s
    print(max)

if __name__=='__main__':
    a =[]
    n = 6
    for i in range(n):
        a.append(list(map(int,input().strip().split())))
    print(list(a))
    hourglassSum(a)
