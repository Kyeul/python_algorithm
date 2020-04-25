# n=int(input())
# x=int(input())
# n, x = map(int, input().split())
n, x = input().split(" ")
n=int(n)
x=int(x)
a= list(map(int, input().split()))

for i in a :
    # print("i=%s"%i)
    if i< x:
        print(i, end=" ")
        # l.append(a[i])
# print(l)

# n, x = map(int, input().split())
# l = list(map(int, input().split()))
#
# for i in l:
#     if i < x:
#         print(i, end=" ")
