'''
A left rotation operation on an array of size n shifts each of the array's elements 1 unit to the left. For example, if 2 left rotations are performed on array , then the array [1,2,3,4,5] would become [3,4,5,1,2].
Given an array of n integers and a number,d , perform d left rotations on the array. Then print the updated array as a single line of space-separated integers.,
'''
if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))
    a2 = [0 for i in range(len(a))]
    for k in range(len(a)):
        a2[k-d] = a[k]
    for i in a2:
        print(i,end=' ')
