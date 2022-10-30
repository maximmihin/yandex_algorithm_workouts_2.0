leg = int(input())
x = list(map(int, input().split()))

if (x[0] <= 0 and x[1] <= 0) and (not(x[0] == 0 and x[1] == 0)):
    print(1)
elif x[0] < 0 and x[1] > 0:
    if leg - x[1] < x[1]:
        print(3)
    else:
        print(1)
elif x[0] > 0 and x[1] < 0:
    if leg - x[0] < x[1]:
        print(2)
    else:
        print(1)
elif x[0] > x[1]:
    if leg % 2 and x[0] + x[1] <= leg + 1:
        print(0)
    elif x[0] + x[1] <= leg:
        print(0)
    else:
        print(3)
elif x[0] <= x[1]:
    if leg % 2 and x[0] + x[1] <= leg + 1:
        print(0)
    elif x[0] + x[1] <= leg:
        print(0)
    else:
        print(2)
