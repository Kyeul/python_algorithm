while 1:
    A, B = map(int, input().split())
    if A > 0 and B < 10:
        break
    else:
        continue

print(A*B)