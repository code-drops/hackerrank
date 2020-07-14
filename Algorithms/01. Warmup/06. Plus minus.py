'''
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.
'''
n = int(input())
a = list(map(int,input().strip().split()))
positive = negative = zeroes = 0
for i in a:
    if i>0:
        positive += 1
    elif i<0:
        negative += 1
    else:
        zeroes += 1
print("{:.6f}".format(positive/n))
print("{:.6f}".format(negative/n))
print("{:.6f}".format(zeroes/n))
