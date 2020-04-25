"""
문제
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N(0 ≤ N ≤ 12)가 주어진다.

출력
첫째 줄에 N!을 출력한다.

예제 입력
10
예제 출력
3628800
"""
def factorial(N) :
    if N == 1 or N == 0:
        return N
    else:
        return factorial(N-1)*N
num = int(input())
print("%s!" %num)
print(factorial(num))

# N=int(input())
# for i in range(1, N):
#     N=N*i
# print(N)

# N = int(input())
# result = 1
# for i in range(1, N+1):
#     result *= i
# print(result)