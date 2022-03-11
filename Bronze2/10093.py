"""
문제
두 양의 정수가 주어졌을 때, 두 수 사이에 있는 정수를 모두 출력하는 프로그램을 작성하시오.

입력
두 정수 A와 B가 주어진다. (1 ≤ A, B ≤ 1015, A와 B의 차이는 최대 100,000)

출력
첫째 줄에 두 수 사이에 있는 수의 개수를 출력한다.

둘째 줄에는 두 수 사이에 있는 수를 오름차순으로 출력한다.
"""

a,b = map(int,input().split())
if a!=b:
    if b<a:
        a,b = b,a

    print(b-a-1)
    for i in range(a+1, b):
        print(i, end=" ")
else:
    print(0)