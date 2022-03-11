"""
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
"""

n =int(input())
num = []
for i in range(0,n):
    number = int(input())
    num.append(number)

num.sort()

for i in num:
    print(i)