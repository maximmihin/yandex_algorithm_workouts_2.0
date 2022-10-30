with open("input.txt") as file:
    N = int(file.readline())
    l = [0] * N
    topics = {}
    for i in range(N):
        tmp_type = int(file.readline())
        if tmp_type == 0:
            l[i] = i
            topics[i] = [file.readline().strip('\n')]
            topics[i].append(0)
        else:
            l[i] = l[tmp_type - 1]
        _ = file.readline()

    for i in range(N):
        topics[l[i]][1] += 1

    print(sorted(list(topics.items()), key=lambda a: (-a[1][1], a[0]))[0][1][0])