a=[]
for s in range(0, 100):
    try:
        a.append(input())
    except EOFError:
        break

for i in a:
    print(i)


