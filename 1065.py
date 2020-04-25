"""
문제
어떤 양의 정수 X의 자리수가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

예제 입력 1
110
예제 출력 1
99
"""

N=int(input())
count=0
for i in range(1, N+1):
    str_num = str(i)
    len_num = len(str_num)
    if len_num==1 or len_num ==2:
        count+=1
    elif len_num == 3 and (int(str_num[1])*2) == (int(str_num[0])+int(str_num[2])):
        count+=1

print(count)

