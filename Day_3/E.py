M = int(input())
M_thing = []
for i in range(M):
    M_thing.append(set(input()))

N = int(input())
N_num = []
N_set = []
for i in range(N):
    N_num.append(input())
    N_set.append(set(N_num[i]))


right_i = []
for i in range(N):
    right_i.append(0)
    for j in range(M):
        if M_thing[j] <= N_set[i]:
            right_i[i] += 1

max_i = max(right_i)
for i in range(N):
    if right_i[i] == max_i:
        print(str(N_num[i]))