'''
Given an array of integers, find the sum of its elements.
'''

def arraysum(a):
    return sum(a)

if __name__=='__main__':
    n = 6
    a = list(map(int,input().strip().split()))
    print(arraysum(a))
