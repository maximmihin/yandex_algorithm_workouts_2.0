N = int(input())
interv = [()] * (N * 2)
for i in range(0, (N * 2), 2):
    tmp = tuple(map(int, input().split()))
    interv[i] = (tmp[0], -1)
    interv[i + 1] = (tmp[1], 1)

interv.sort()

color_layer = 0
colored = 0
for i in range(len(interv)):
    if color_layer > 0:
        colored += interv[i][0] - interv[i - 1][0]
    if interv[i][1] == -1:
        color_layer += 1
    else:
        color_layer -= 1

print(colored)