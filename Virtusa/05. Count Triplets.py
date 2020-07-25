'''
You are given an array and you need to find number of tripets of indices (i,j,k) such that the elements at those indices are in geometric progression for a given common ratio r and i<j<k.
For example,arr=[1,4,16,64] . If r=4, we have [1,4,16] and [4,16,64] at indices (0,1,2) and (1,2,3).
'''

from collections import defaultdict
n, r = map(int, input().split())
arr = list(map(int, input().split()))
m1, m2 = defaultdict(int), defaultdict(int)
triplets = 0
for i in reversed(arr):
    if (i * r) in m2:
        triplets += m2[i * r]
    if (i * r) in m1:
        m2[i] += m1[i * r]
    m1[i] += 1
print(triplets)
