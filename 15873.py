"""
자연수 A, B가 주어지면 A+B를 구하는 프로그램을 작성하시오.

입력
자연수 A, B (0 < A, B ≤ 10)가 첫 번째 줄에 주어진다. 단, 두 수의 사이에는 공백이 주어지지 않는다. 두 수의 앞에 불필요한 0이 붙는 경우는 없다.

출력
첫 번째 줄에 A+B의 값을 출력한다.

예제 입력 1
37
예제 출력 1
10
"""
s=input()
r=0
for i in range(0, len(s)):
    if int(s[i]) == 0:
        r += 9
    r += int(s[i])
print(r)