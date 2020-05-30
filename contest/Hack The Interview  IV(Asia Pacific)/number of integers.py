/*

Given two large integers, L and R, find the number of integers greater than L and less than or equal to R exactly K non-zero digits.

For example, consider the two integers to be,l=2  and r=15 and k=1, the integers [3, 4, 5, 6, 7, 8, 9, 10] contain exactly 1 non-zero digit.

*/
l = int(input("left bound : "))
r = int(input("right bound : "))
k = int(input("non zero digit : "))
numbers = []
for i in range(l+1,r+1):
    numbers.append(i)
numbers = list(map(lambda x:str(x),numbers))

count = 0
valid =[]
for i in numbers:
    count = 0
    for j in range(0,len(i)):
        if i[j]!="0":
            count = count +1
    if count == k:
        valid.append(i)
print(len(valid))
