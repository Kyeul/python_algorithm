while 1:
    try:
        A, B = map(int, input().split())
        if A>0 and B>0:
            print(A+B)
        elif A == 0 and B ==0 :
            exit()
        else:
            continue
    except EOFError:
        break