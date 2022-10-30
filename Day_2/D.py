L, K = map(int, input().split())
legs = list(map(int, input().split()))
med_L = L // 2
even_flag = bool(L % 2)

for i in range(K):
    if legs[i] == med_L and even_flag:
        print(legs[i])
        break
    elif legs[i] >= med_L:
        print(max(legs[:i]), min(legs[i:]))
        break