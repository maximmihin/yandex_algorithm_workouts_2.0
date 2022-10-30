ex_code = int(input())
ve_inter = int(input())
ve_check = int(input())

if ve_inter == 0:
    if ex_code != 0:
        print(3)
    else:
        print(ve_check)
elif ve_inter == 1:
    print(ve_check)
elif ve_inter == 4:
    if ex_code != 0:
        print(3)
    else:
        print(4)
elif ve_inter == 6:
    print(0)
elif ve_inter == 7:
    print(1)
else:
    print(ve_inter)
