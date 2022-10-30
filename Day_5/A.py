n, q = list(map(int, input().split()))
seq_n = list(map(int, input().split()))

seq_q = [[]] * q
for i in range(q):
    tmp_inp = input().split()
    tmp_inp[0] = int(tmp_inp[0])
    tmp_inp[1] = int(tmp_inp[1])
    seq_q[i] = tmp_inp
pref_seq_n = [0] * (n + 1)
for i in range(1, n + 1):
    pref_seq_n[i] = pref_seq_n[i - 1] + seq_n[i - 1]

for i in range(q):
    print(pref_seq_n[seq_q[i][1]] - (pref_seq_n[seq_q[i][0] - 1]))