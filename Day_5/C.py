with open("input.txt") as file:
    n, m = list(map(int, file.readline().split()))
    tmp_n = file.readline().split()
    n_seq = [[int(tmp_n[i]), i] for i in range(n)]
    tmp_m = file.readline().split()
    m_seq = [[int(tmp_m[i]), i] for i in range(m)]

n_seq.sort()
m_seq.sort()

i = 0
j = 0
ret = [0] * n
while i < n:
    while j < m:
        if n_seq[i][0] < m_seq[j][0]:
            ret[n_seq[i][1]] = m_seq[j][1] + 1
            i += 1
        j += 1
    i += 1

p = 0
for i in range(n):
    if ret[i] != 0:
        p += 1
print(p)

for i in range(n):
    print(ret[i], end=' ')
print()