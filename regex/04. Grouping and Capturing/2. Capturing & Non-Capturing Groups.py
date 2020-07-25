'''
You have a test String S.
Your task is to write a regex which will match S with the following condition:
S should have 3 or more consecutive repetitions of ok.
'''

Regex_Pattern = r'(ok){3,}'	# Do not delete 'r'.
import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())
