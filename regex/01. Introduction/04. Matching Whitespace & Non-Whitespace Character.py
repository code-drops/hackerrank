#You have a test string S . Your task is to match the pattern XXxXXxXX
#Here,x  denotes whitespace characters, and X denotes non-white space characters.


Regex_Pattern = r"\S\S\s\S\S\s\S\S"	# Do not delete 'r'.
import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())
