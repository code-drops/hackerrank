'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
'''

if __name__ == '__main__':
    n = int(input())
    s = [int(i) for i in input().strip().split()]
    s = sorted(s,reverse=True)
    for i in range(1,len(s)):
        if s[0]!=s[i]:
            print(s[i])
            break
