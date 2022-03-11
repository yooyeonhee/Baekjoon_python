"""
문제
두 정수 a와 b 최소공배수는 두 수의 공통된 배수 중 가장 작은 수이고, 최대공약수는 두 수의 공통된 약수중 가장 큰 수이다.

a와 b가 주어졌을 때, 최소공배수와 최대공약수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T(1<=T<=1,000)가 주어진다. 각 테스트 케이스는 두 정수 a와 b로 이루어져 있고, 공백으로 구분되어 있다. (1 <= a,b <= 1,000)

출력
각 테스트 케이스에 대해 최소공배수와 최대공약수를 차례대로 출력한다.
"""


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


T = int(input())
for _ in range(0, T):
    A, B = map(int, input().split())
    if A > B:
        A, B = B, A
    print(lcm(A, B), gcd(A, B))
