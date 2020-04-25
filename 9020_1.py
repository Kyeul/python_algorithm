"""
 짝수를 두 소수의 합으로 나타내는 표현을 그 숫자의 골드바흐 파티션이라고 한다. 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다. 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.

2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고 짝수 n이 주어진다. (4 ≤ n ≤ 10,000)

출력
각 테스트 케이스에 대해서 주어진 n의 골드바흐 파티션을 출력한다. 출력하는 소수는 작은 것부터 먼저 출력하며, 공백으로 구분한다.

예제 입력 1
3
8
10
16
예제 출력 1
3 5
5 5
5 11
"""
import sys

def generator(n):
    # for i in range(2, n + 1):
    #     b = True
    #     for j in l1:
    #         if i % j == 0:
    #             b = False
    #             break
    #         elif j > i ** 0.5:
    #             break
    #     if b:
    #         yield i
    l1 = (2, i for i in range(3, n+1, 2))
    for i in l1:
        if i*i > n:
            break
        for j in range(3, n+1, 2):
            if i*j > n:
                break
            try:
                l1.remove(i*j)
            except ValueError:
                continue

t = int(sys.stdin.readline()) #testcase input
a = 1
while a <= t:
    a += 1
    l2 = []
    l3 = []
    n = int(sys.stdin.readline())
    l1 = generator(n)

    for i in l1:
        for j in l1[i:]:
            if i + j > n:
                break
            if i + j == n:
                l2.append(i)
                l2.append(j)
    sys.stdout.write("%s %s" % (l2.pop(), l2.pop()))
