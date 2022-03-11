"""
정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.
"""

num = int(input())
list = []
N = 2
while num!=1:
    if num%N==0:
        num/=N
        list.append(N)
        N=2
    else:
        N+=1
for i in list:
    print(i)