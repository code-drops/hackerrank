'''
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
'''

if __name__=='__main__':
    n = int(input())
    a = []
    for i in range(n):
        a.append([input(),float(input())])
    score = set([i[1] for i in a])
    score.remove(min(score))
    m = min(score)
    names =[]
    for i in a:
        if m==i[1]:
            names.append(i[0])
    for i in sorted(names):
        print(i)
