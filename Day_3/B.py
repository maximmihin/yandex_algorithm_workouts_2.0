seq = list(input().split())

s = set()
for i in range(len(seq)):
    if seq[i] in s:
        print('YES')
    else:
        print('NO')
    s.add(seq[i])