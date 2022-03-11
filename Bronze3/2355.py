"""
문제
두 정수 A와 B가 주어졌을 때, 두 정수 사이에 있는 수의 합을 구하는 프로그램을 작성하시오. 사이에 있는 수들은 A와 B도 포함한다.

입력
첫째 줄에 두 정수 A, B가 주어진다. (-2,147,483,648 ≤ A, B ≤ 2,147,483,647)

출력
첫째 줄에 답을 출력한다. (-2,147,483,648 ≤ 답 ≤ 2,147,483,647)
"""

import sys
A,B = map(int, sys.stdin.readline().split())
if A>B:
    A,B = B,A
if A<0 and B>=0:
    n = abs(A)+B+1
elif A<0 and B<=0:
    n = abs(A-B)+1
elif A>=0 and B>=0:
    n = abs(B-A)+1
print(n*(A+B)//2)