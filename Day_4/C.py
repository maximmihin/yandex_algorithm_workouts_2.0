d = {}
with open("input.txt") as file:
    for line in file:
        l_words = line.split()
        for i in range(len(l_words)):
            if l_words[i] not in d:
                d[l_words[i]] = 0
            d[l_words[i]] -= 1

it = list(d.items())


def my_sort(l):
    return l[1], l[0]


it.sort(key=my_sort)
for i in range(len(it)):
    print(it[i][0])