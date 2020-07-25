'''
You have a test string S.
Your task is to write a regex that will match S  using the following conditions:

S should begin with 2 or more digits.
After that, S should have  or more lowercase letters.
S should end with 0 or more uppercase letters
 '''
 
 Regex_Pattern = r'^\d{2,}[a-z]{0,}[A-Z]{0,}$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
