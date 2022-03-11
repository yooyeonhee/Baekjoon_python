"""
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
"""

num1, num2  = map(int, input().split())
tmp=0
if num1 <num2:
    tmp = num2
    num2 = num1
    num1 = tmp
def gcd(a,b):
    while b!=0:
        a,b = b, a%b
    return a
def lcm(a,b):
    return a*b//gcd(a,b)
print(gcd(num1, num2))
print(lcm(num1, num2))