'''
Calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.
'''
def aVeryBigSum(ar):
    return sum(ar)
if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    print(aVeryBigSum(ar))
