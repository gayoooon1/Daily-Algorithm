try:
    while 1:
        a, b = map(int, input().split())
        if (a==0) & (b==0): break
        elif (a<0) | (b>10): break
        print(a+b)
except:
    exit()
# try, except 활용 문제