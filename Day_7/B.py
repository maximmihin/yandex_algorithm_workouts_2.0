n = int(input())
interv = [()] * (n * 2)
for i in range(0, (n * 2), 2):
    tmp = tuple(map(int, input().split()))
    interv[i] = (tmp[0], 1)
    interv[i + 1] = (tmp[0] + tmp[1], -1)

interv.sort()

stan = 0
max_stan = 0
for i in range(len(interv)):
    if interv[i][1] == 1:
        stan += 1
    else:
        stan -= 1
    max_stan = max(max_stan, stan)

print(max_stan)