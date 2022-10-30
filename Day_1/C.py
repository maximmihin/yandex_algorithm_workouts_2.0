x = list(map(int, input().split()))

if x[0] > 12 or x[1] > 12 or x[0] == x[1]:
    print(1)
else:
    print(0)
