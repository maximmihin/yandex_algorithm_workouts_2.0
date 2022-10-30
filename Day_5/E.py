S = int(input())

def get_seq(S, W):

    inp = input().split()
    len_inp = len(inp) - 1
    yyy_seq = [()] * len_inp
    max_val = S - 1
    j = 0

    for i in range(len_inp):
        tmp = int(inp[i + 1])
        if tmp < max_val:
            yyy_seq[j] = (tmp, i)
            j += 1

    for k in range(len_inp - j):
        yyy_seq.pop()

    def c_sort(seq):
        return seq[0], -seq[1]

    if W == 'C':
        yyy_seq.sort(key=c_sort, reverse=True)
    else:
        yyy_seq.sort()

    seq = [()] * len(yyy_seq)
    seq[0] = yyy_seq[0]
    j = 1
    for i in range(1, len(yyy_seq)):
        if yyy_seq[i][0] != yyy_seq[i - 1][0]:
            seq[j] = yyy_seq[i]
            j += 1
    for k in range(len(yyy_seq) - j):
        seq.pop()
    return seq


A_seq = get_seq(S, 'A')
B_seq = get_seq(S, 'B')
C_seq = get_seq(S, 'C')


first_entry_C = 0
C_R = len(C_seq)
ret = [16000, 16000, 16000]
for aval, aind in A_seq:

    k = first_entry_C
    flag_first_entry_C = True

    for bval, bind in B_seq:
        C_find = S - (aval + bval)
        if C_find < 1:
            break
        while k < C_R:
            if C_seq[k][0] > C_find:
                k += 1
                continue
            if C_seq[k][0] == C_find:
                ret = min(ret, [aind, bind, C_seq[k][1]])
                k += 1
            if flag_first_entry_C:
                first_entry_C = k
                flag_first_entry_C = False
            break

if ret == [16000, 16000, 16000]:
    print(-1)
else:
    print(ret[0], ret[1], ret[2])