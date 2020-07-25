'''
Write a regex which can match all the occurences of characters which are not immediately preceded by vowels (a, e, i, u, o, A, E, I, O, U).
'''
Regex_Pattern = r"(?<![aeiouAEIOU])."
import re
Test_String = input()
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))
