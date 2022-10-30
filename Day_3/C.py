seq = list(input().split())

s1 = set()
s2 = set()
for i in range(len(seq)):
    if seq[i] not in s1:
        s1.add(seq[i])
    else:
        s2.add(seq[i])

l = []
s1 -= s2
for i in range(len(seq)):
    if seq[i] in s1:
      l.append(seq[i])
      s1.remove(seq[i])
    if len(s1) == 0:
        break
print(' '.join(l))
