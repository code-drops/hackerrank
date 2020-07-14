'''
Given an integer,n , and n space-separated integers as input, create a tuple,t , of those n integers. Then compute and print the result of hash(t).
'''
n = int(input())
a = list(map(int,input().strip().split()))
print(hash(tuple(a)))
