yut_list = [list(map(int, input().split())) for _ in range(3)]
sum_list = list(map(sum, yut_list))
for a in sum_list:
    if a == 0: print("D")
    elif a == 1: print("C")
    elif a == 2: print("B")
    elif a == 3: print("A")
    elif a == 4: print("E")