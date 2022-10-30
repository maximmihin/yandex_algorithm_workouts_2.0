N = set(range(1, int(input()) + 1))
while True:
    s1 = input()
    if s1 == 'HELP':
        print(' '.join(map(str, sorted(list(N)))))
        break
    s2 = input()
    if s2 == 'YES':
        N.intersection_update(set(map(int, s1.split())))
    else:
        N.difference_update(set(map(int, s1.split())))