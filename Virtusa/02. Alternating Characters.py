'''
You are given a string containing characters A and B only. Your task is to change it into a string such that there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.
Your task is to find the minimum number of required deletions.
For example, given the string s = AABAAB, remove an A at positions 0 and 3 to make s = ABAB in 2 deletions.
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    s = list(s)
    n = len(s)
    flag = 'A' if s[0]=='A' else 'B'
    i = 1
    while i<= len(s)-1:
        if s[i]==flag:
            s.pop(i)
        else:
            i += 1
            if flag=='A':
                flag = 'B'
            else:
                flag = 'A'
    return (n - len(s))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
