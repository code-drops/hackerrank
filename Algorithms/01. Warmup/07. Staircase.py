'''
Consider a staircase of size n=4:
   #
  ##
 ###
####
Observe that its base and height are both equal to n, and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size n.
'''

n = int(input())
for i in range(n):
    for tab in range(n-i-1):
        print(' ',end='')
    for k in range(i+1):
        print('#',end='')
    print()
