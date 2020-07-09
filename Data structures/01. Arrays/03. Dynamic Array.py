'''
Create a list, seqlist , of n empty sequences, where each sequence is indexed from 0 to n-1. The elements within each of the n sequences also use 0-indexing.
Create an integer, lastAnswer , and initialize it to 0.
The 2 types of queries that can be performed on your list of sequences (seqlist) are described below:
Query: 1 x y
->Find the sequence,seq , at index ((x ^ lastAnswer)%n) in seqlist.
->Append integer y to sequence seq.
Query: 2 x y
->Find the sequence,seq , at index ((x ^ lastAnswer)%n) in seqlist.
->Find the value of element y%size in seq (where size is the size of seq) and assign it to lastAnswer.
->Print the new value of lastAnswer on a new line

'''

def dynamicArray(n, queries):
    seq = []
    lastAnswer = 0
    for i in range(n):
        seq.append([])
    for i in queries:
        if i[0]==1:
            s = (i[1]^lastAnswer)%n
            seq[s].append(i[2])
        elif i[0]==2:
            s = (i[1]^lastAnswer)%n
            lastAnswer = seq[s][i[2] % len(seq[s])]
            print(lastAnswer)

n,q = list(map(int,input().strip().split()))
queries = []
for i in range(q):
    queries.append(list(map(int,input().strip().split())))
dynamicArray(n,queries)
