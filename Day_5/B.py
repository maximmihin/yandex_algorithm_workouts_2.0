n = int(input())
seq = list(map(int, input().split()))

pref_sum = [0] * (n + 1)
for i in range(1, (n + 1)):
    if pref_sum[i - 1] <= 0:
        pref_sum[i] = seq[i - 1]
    else:
        pref_sum[i] = pref_sum[i - 1] + seq[i - 1]
print(max(pref_sum[1:]))