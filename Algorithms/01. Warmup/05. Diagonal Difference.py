'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
For example, the square matrix  is shown below:
1 2 3
4 5 6
9 8 9
The left-to-right diagonal = 1+5+9=15 . The right to left diagonal = 3+5+9=17. Their absolute difference is |15-17|=2.
'''
if __name__ == '__main__':
    n = int(input().strip())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))
        d1 = 0
        d2 = 0
    for i in range(n):
        for j in range(n):
            if i==j:
                d1 += a[i][i]
            if i+j == (n-1):
                d2 += a[i][j]
    print(abs(d1-d2))
