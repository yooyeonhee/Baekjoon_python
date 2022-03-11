"""
문제
성민이는 이번 학기에 미적분학 과목을 수강하고 있다. 다항함수의 미분 단원 과제를 하던 도중 미분을 하기가 귀찮아진 성민이는 미분하려는 함수 f(x)가 주어지면, 미분 된 함수 f’(x)를 자동으로 구해주는 프로그램을 만들어서 계산을 줄일 생각을 하였다. 우리도 성민이가 원하는 프로그램을 한번 같이 만들어보도록 하자.

입력
첫째 줄에는 항의 개수 N(1 ≤ N ≤ 100)이 주어진다.

둘째 줄부터 N개 줄에 걸쳐서 항의 계수 C(-100 ≤ C ≤ 100, C ≠ 0)와 항의 차수 K(0 ≤ K ≤ 1000)가 항의 차수가 큰 순서대로 주어진다. 항의 차수가 같은 항은 2개 이상 존재하지 않는다.

출력
f’(1)의 값을 첫째 줄에 출력한다.

"""
t = int(input())
sic = []
result = 0
for _ in range(t):
    C, K = map(int, input().split())
    if K - 1 >= 0:
        sic.append(C * K)
for i in sic:
    result = result + i * 1
print(result)