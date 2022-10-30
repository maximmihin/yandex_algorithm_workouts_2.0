inp = input()

i = 0
price = 0
for j in range(len(inp) - 1, (len(inp) - 1) // 2, -1):
    if inp[i] != inp[j]:
        price += 1
    i += 1

# j = len(inp) - 1
# while i <= j:
#     if inp[i] != inp[j]:
#         price += 1
#     i += 1
#     j -= 1

print(price)