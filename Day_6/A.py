with open('input.txt') as file:
    _ = file.readline()
    seq = list(map(int, file.readline().split()))
    seq.sort()

    q = int(file.readline())
    query_list = [[]] * q
    for i in range(q):
        tmp_inp = file.readline().split()
        query_list[i] = [int(tmp_inp[0]), int(tmp_inp[1])]


def my_check(m, checkparam):
    seq, f = checkparam[0], checkparam[1]
    return seq[m] >= f


def my_check2(m, checkparam):
    seq, f = checkparam[0], checkparam[1]
    return seq[m] <= f


def lbinsearch(l, r, check, checkparam):
    while l < r:
        m = (r + l) // 2
        if check(m, checkparam):
            r = m
        else:
            l = m + 1
    return r


def rbinsearch(l, r, check, checkparam):
    while l < r:
        m = (r + l + 1) // 2
        if check(m, checkparam):
            l = m
        else:
            r = m - 1
    return l


def get_left_entry(l, r, check, checkparam):
    left_entry = lbinsearch(l, r, check, checkparam)
    seq, f = checkparam

    if left_entry == len(seq) - 1 and seq[left_entry] < f:
        return left_entry, False
    return left_entry, True


def get_right_entry(l, r, check, checkparam):
    right_entry = rbinsearch(l, r, check, checkparam)
    seq, f = checkparam

    if right_entry == 0 and seq[right_entry] > f:
        return right_entry, False
    return right_entry, True


for l_q, r_q in query_list:
    left_entry = get_left_entry(0, len(seq) - 1, my_check, (seq, l_q))
    right_entry = get_right_entry(0, len(seq) - 1, my_check2, (seq, r_q))
    if left_entry[1] == False or right_entry[1] == False:
        print(0, end=' ')
    else:
        print(right_entry[0] - left_entry[0] + 1, end=' ')
print()