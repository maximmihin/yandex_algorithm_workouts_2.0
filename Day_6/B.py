with open("input.txt") as file:
    _ = file.readline()
    seq = tuple(map(int, file.readline().split()))
    _ = file.readline()
    query_list = tuple(map(int, file.readline().split()))


def my_check1(m, checkparam):
    seq, f = checkparam
    return seq[m] >= f


def my_check2(m, checkparam):
    seq, f = checkparam
    return seq[m] <= f


def lbinsearch(l, r, check, checkparam):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparam):
            r = m
        else:
            l = m + 1
    return l


def rbinsearch(l, r, check, checkparam):
    while l < r:
        m = (l + r + 1) // 2
        if check(m, checkparam):
            l = m
        else:
            r = m - 1
    return l


def get_left(f, seq):
    left = lbinsearch(0, len(seq) -1, my_check1, (seq, f))
    if seq[left] != f:
        return -1
    return left

def get_right(f, seq):
    right = rbinsearch(0, len(seq) - 1, my_check2, (seq, f))
    if seq[right] != f:
        return -1
    return right


for q in query_list:
    left = get_left(q, seq) + 1
    right = get_right(q, seq) + 1
    print(left, right)