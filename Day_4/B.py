i = 0
d = {}
with open("input.txt") as file:
    for line in file:
        key, var = line.split()
        if key not in d:
            d[key] = 0
        d[key] += int(var)
s_keys = list(sorted(d.keys()))
for i in range(len(s_keys)):
    print(s_keys[i], d[s_keys[i]])