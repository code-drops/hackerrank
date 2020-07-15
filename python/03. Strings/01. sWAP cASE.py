'''
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
'''
def swap_case(s):
    temp =''
    for i in range(len(s)):
        if s[i].isupper():
            temp = temp + s[i].lower()
        else:
            temp = temp + s[i].upper()
    return temp

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
