'''
Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.
For example, the note is "Attack at dawn". The magazine contains only "attack at dawn". The magazine has all the right words, but there's a case mismatch. The answer is "No".
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    hashcode = {}
    for word in magazine:
        if hashcode.get(word)!=None:
            hashcode[word] += 1
        else:
            hashcode[word] = 1
    for word in note:
        if hashcode.get(word)==None or hashcode[word]==0:
            return 'No'
        else:
            hashcode[word] += -1
    return 'Yes'



if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))
