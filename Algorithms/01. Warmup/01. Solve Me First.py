'''
Complete the function solveMeFirst to compute the sum of two integers.
'''
if __name__ == '__main__':
    n = int(input())
    l = input().strip().split()
    l = [int(i) for i in l]
    for i in l[-1::-1]:
        print(i,end=' ')
