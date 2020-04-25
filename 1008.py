while 1:
    A, B = map(int, input().split())
    if A >= 1 and B <= 10000 and B !=0 :
        break
    else:
        continue

print(A/B)