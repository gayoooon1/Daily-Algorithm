num = int(input())
num_list = [int(input()) for _ in range(num)]
for a in sorted(num_list):
    print(a)