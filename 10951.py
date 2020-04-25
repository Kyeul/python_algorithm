while 1:
    try:
        A, B = map(int, input().split())
        if A>0 and B>0:
            print(A+B)
        else:
            continue
    except EOFError:
        break