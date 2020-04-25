"""
문제
세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 세 정수 A, B, C가 공백으로 구분되어 주어진다. (1 ≤ A, B, C ≤ 100)

출력
두 번째로 큰 정수를 출력한다.

예제 입력 1
20 30 10
예제 출력 1
20
예제 입력 2
30 30 10
예제 출력 2
30
"""
A,B,C=map(int, input().split())

if A>= B and A>= C:
    if B>= C:
        print(B)
    else:
        print(C)
elif B>=A and B>=C:
    if A>=C:
        print(A)
    else:
        print(C)
else:
    if A>=B:
        print(A)
    else:
        print(B)