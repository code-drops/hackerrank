'''
Your task is to write a regular expression that matches only and exactly strings of form: abc.def.ghi.jkx, where each variable a,b,c,d,e,f,g,h,i,j,k,x can be any single character except the newline.
'''

regex_pattern = r"^.{3}\..{3}\..{3}\..{3}$"	# Do not delete 'r'.

import re
import sys

test_string = input()

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())
