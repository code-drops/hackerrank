/*

You have been given a binary string containing only the characters "0" and "1". A binary string is considered valid if each of its substrings of at least a certain length contains at least one "1" character. Given the binary string, and the minimum length of substring, determine how many characters of the string need to be changed in order to make the binary string valid.

Note that string v is a substring of string w if it has a non-zero length and can be read starting from some position in string w. For example, string "010" has six substrings: "0", "1", "0", "01", "10", "010".

For example, let's say the binary string  = "0001" of length n=4, and the minimum substring length is d=2. This is currently not valid because one of its substrings, "000", of length 3 has no "1"s in it. By changing the second character to a "1", the string becomes "0101". In this case, all of its substrings of length 2 or more has at least one "1" character: "01", "10", and "01". Because this required 1 change, the answer is 1.

*/

string = input()
length = int(input())
change = 0
count = 0
for i in range(0, len(string)):
    if string[i] == "1":
        count = 0
    elif string[i]=="0":
        count = count + 1
        if count == length:
            string[i]==1
            change = change+1
            count = 0
print(change)
