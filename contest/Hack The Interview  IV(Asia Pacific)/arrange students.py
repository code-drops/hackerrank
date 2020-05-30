/*

A classroom has several students, half of whom are boys and half of whom are girls. You need to arrange all of them in a line for the morning assembly such that the following conditions are satisfied:

The students must be in order of non-decreasing height.
Two boys or two girls must not be adjacent to each other.
You have been given the heights of the boys in the array  and the heights of the girls in the array . Find out whether you can arrange them in an order which satisfies the given conditions. Print "YES" if it is possible, or "NO" if it is not.

For example, let's say there are n=3 boys and n=3 girls, where the boys' heights are b=[5,3,8] and the girls' heights are g =[2,4,6]. These students can be arranged in the order [2, 3, 4, 5, 6, 8]. Because this is in order of non-decreasing height, and no two boys or two girls are adjacent to each other, this satisfies the conditions. Therefore, the answer is "YES".

*/

test_case = int(input())
for test in range(1,test_case+1):
    number = int(input())
    boys = input()
    boys = boys.split(" ")
    boys = list(map(lambda x: int(x), boys))
    boys = list(sorted(boys))

    girls = input()
    girls = girls.split(" ")
    girls = list(map(lambda x: int(x), girls))
    girls = list(sorted(girls))
    final = []

    while boys!=[] and girls!=[]:
        if boys[0]<girls[0]:
            final.append(boys[0])
            final.append(girls[0])
            boys.pop(0)
            girls.pop(0)
        else:
            final.append(girls[0])
            final.append(boys[0])
            boys.pop(0)
            girls.pop(0)
    for i in range(1, len(final)):
        if final[i - 1] <= final[i]:
            flag = True
        else:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")
