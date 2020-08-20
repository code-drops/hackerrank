'''
You are given a string S.
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
In the second line, print True if S has any alphabetical characters. Otherwise, print False.
In the third line, print True if S has any digits. Otherwise, print False.
In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.
'''

s = input()
output = [False for i in range(0,5)]
for i in range(0, len(s)):
    if s[i].isalnum():
        output[0] = True
    if s[i].isalpha():
        output[1] = True
    if s[i].isdigit():
        output[2] = True
    if s[i].islower():
        output[3] = True
    if s[i].isupper():
        output[4] = True
for i in output:
    print(i)
