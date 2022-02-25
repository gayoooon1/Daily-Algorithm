while True:
        a,b,c = input().split()
        sort_list = sorted([int(a),int(b),int(c)])
        if (int(a)==0) & (int(b)==0) & (int(c)==0):
            break
        elif sort_list[0]**2 + sort_list[1]**2 != sort_list[2]**2: 
            print('wrong')
            continue
        elif sort_list[0]**2 + sort_list[1]**2 == sort_list[2]**2:
            print('right')
            continue