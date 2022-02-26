num = int(input())
vote_list = [int(input()) for _ in range(num)]
y_cute=0
n_cute=0
for a in vote_list:
    if a == 1: y_cute+=1
    elif a == 0: n_cute+=1
if y_cute > n_cute: print("Junhee is cute!")
else: print("Junhee is not cute!")