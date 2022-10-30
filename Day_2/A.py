seq = [(int(input()))]
i = 0
while seq[i] != 0:
    seq.append(int(input()))
    i += 1
if i == 0:
    print(0)
else:
    biggest = seq[0]
    num_biggest = 1

    for i in range(1, len(seq) - 1):
        if seq[i] > biggest:
            biggest = seq[i]
            num_biggest = 1
        elif seq[i] == biggest:
            num_biggest += 1
    print(num_biggest)
