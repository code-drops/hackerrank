'''
It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! There are a number of people queued up, and each person wears a sticker indicating their initial position in the queue. Initial positions increment by 1 from 1 at the front of the line to n at the back.
Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap positions, they still wear the same sticker denoting their original places in line. One person can bribe at most two others. For example, if person 5 and person 4 bribes , the queue will look like this: 1,2,3,5,4,6,7,8.
Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get the queue into its current state!
'''
test_cases = int(input())
for _ in range(test_cases):
    t = int(input())
    a = list(map(int, input().split()))
    swaps = [0] * t

    swapped = True

    while swapped:
        swapped = False

        for i in range(t):
            while i < t - 1 and a[i] > a[i + 1]:
                swaps[a[i] - 1] += 1
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
                i += 1

    s = 0
    for swap in swaps:
        s += swap

        if swap > 2:
            print('Too chaotic')
            break
    else:
        print(s)
