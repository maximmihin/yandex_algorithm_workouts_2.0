n = int(input())
d = {}
keys = [0] * n
for i in range(n):
    keys[i], value = map(int, input().split())
    if keys[i] not in d:
        d[keys[i]] = 0
    d[keys[i]] += value

s_keys = sorted(list(set(keys)))
for i in range(len(d)):
    print(s_keys[i], d[s_keys[i]])