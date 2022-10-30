d ={}
all_votes = 0
with open("input.txt") as file:
    for line in file:
        tmp_k, tmp_v = line.rsplit(' ', 1)
        d[tmp_k] = [int(tmp_v)]
        all_votes += d[tmp_k][0]

perv_izb_ch = 450 / all_votes
key_list = list(d.keys())
for i in range(len(d.keys())):
    d[key_list[i]].append(d[key_list[i]][0] * perv_izb_ch)
    d[key_list[i]].append(d[key_list[i]][1] % 1)

ost_golosov = 450 - sum([int(d[key_list[i]][1]) for i in range(len(d.keys()))])
if ost_golosov:
    n_d = [[]] * len(d)
    for i in range(len(d)):
        n_d[i] = [tuple((d[key_list[i]][2], -d[key_list[i]][0]))]
        n_d[i].append(d[key_list[i]])

    n_d.sort(reverse=True)
    for i in range(len(n_d)):
        n_d[i][1][1] += 1
        ost_golosov -= 1
        if not ost_golosov:
           break

for i in range(len(key_list)):
    print(key_list[i], int(d[key_list[i]][1]))