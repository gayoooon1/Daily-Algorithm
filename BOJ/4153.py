def Triangle():
    while True:
        a,b,c = input().split()
        if (int(a)==0) & (int(b)==0) & (int(c)==0):
            break
        elif int(a)**2 + int(b)**2 != int(c)**2: 
            print('wrong')
            continue
        elif int(a)**2 + int(b)**2 == int(c)**2:
            print('right')
            continue


Triangle()

