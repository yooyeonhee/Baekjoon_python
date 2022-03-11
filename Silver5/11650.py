"""
2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
"""

N = int(input())
ja =[]
for i in range(N):
    x, y = map(int, input().split())
    ja.append((x,y))
re = sorted(ja)
for j in range(N):
    print(re[j][0], re[j][1])
