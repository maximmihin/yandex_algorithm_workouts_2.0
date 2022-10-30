x = list(map(int, input().split()))

if x[1] < x[2]:
    x[1], x[2] = x[2], x[1]

a_rez = x[1] - x[2] - 1
b_rez = x[0] - a_rez - 2

if a_rez < b_rez:
    print(a_rez)
else:
    print(b_rez)
