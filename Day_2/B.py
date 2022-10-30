seq = list(map(int, input().split()))
max_len = 0


def find_max_len_to_shop(seq, index):
    to_l = 10
    for i in range(index - 1, -1, -1):
        if seq[i] == 2:
            to_l = index - i
            break
    to_r = 10
    for i in range(index + 1, 10):
        if seq[i] == 2:
            to_r = i - index
            break
    return min(to_l, to_r)


for i in range(10):
    if seq[i] == 1:
        tmp_max = find_max_len_to_shop(seq, i)
        max_len = max(max_len, tmp_max)

print(max_len)
