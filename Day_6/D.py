inp = tuple(map(int, input().split()))


def axe_check(m, checkparam):
    a, k_d, b, m_d, x = checkparam

    d_rub = (a * (m - (m // k_d)))
    f_rub = (b * (m - (m // m_d)))

    return (d_rub + f_rub) >= x


def lbinsearch(l, r, check, checkparam):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparam):
            r = m
        else:
            l = m + 1
    return l


def fbinsearch(l, r, eps, check, checkparam):
    while l + eps < r:
        m = (l + r) / 2
        if check(m, checkparam):
            r = m
        else:
            l = m
    return l

start = 0
stop = 2
while True:
    ret = lbinsearch(start, stop, axe_check, inp)
    if axe_check(ret, inp):
        break
    start, stop = stop, stop ** 2
print(ret)