'''
input rows and columns
output the following pattern: 
r = 9 , c = 27
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
'''

n,m = tuple(map(int,input().strip().split()))
pattern = '.|.'
for i in range(0,n//2):
    s = pattern*(2*i+1)
    print(s.center(m,'-'))
print('WELCOME'.center(m,'-'))
for i in range(n//2-1,-1,-1):
    s = pattern*(2*i+1)
    print(s.center(m,'-'))
