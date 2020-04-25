T=int(input())
for i in range(0, T):
    A, B= map(int, input().split())
    if A>0 and B>0:
        print("Case #%d: %d + %d = %d" %(i+1,A, B ,(A+B)))
    else:
        continue