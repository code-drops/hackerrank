'''
There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings.
For example, given input strings=['ab','ab','abc'] and ,queries=['ab','abc','bc'] we find 2 instances of 'ab',1 of 'abc' and 0 of 'bc'. For each query, we add an element to our return array,result = [2,1,0] .
'''
if __name__ == '__main__':
    n = int(input())
    strings = [input() for i in range(n)]
    m = int(input())
    query = [input() for i in range(m)]
    l = [0 for i in range(m)]
    for i in range(m):
        if query[i] in strings:
            l[i] = strings.count(query[i])
    for i in l:
        print(i)
