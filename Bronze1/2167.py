"""
문제
2차원 배열이 주어졌을 때 (i, j) 위치부터 (x, y) 위치까지에 저장되어 있는 수들의 합을 구하는 프로그램을 작성하시오. 배열의 (i, j) 위치는 i행 j열을 나타낸다.

입력
첫째 줄에 배열의 크기 N, M(1 ≤ N, M ≤ 300)이 주어진다. 다음 N개의 줄에는 M개의 정수로 배열이 주어진다. 배열에 포함되어 있는 수는 절댓값이 10,000보다 작거나 같은 정수이다. 그 다음 줄에는 합을 구할 부분의 개수 K(1 ≤ K ≤ 10,000)가 주어진다. 다음 K개의 줄에는 네 개의 정수로 i, j, x, y가 주어진다(i ≤ x, j ≤ y).

출력
K개의 줄에 순서대로 배열의 합을 출력한다. 배열의 합은 231-1보다 작거나 같다.
"""
N, M = map(int, input().split())
ip = []
ba = [[0] * (M + 1) for _ in range(N + 1)]
for _ in range(N):
    ip.append(list(map(int, input().split())))
for i in range(1, N + 1):
    for j in range(1, M + 1):
        ba[i][j] = ip[i - 1][j - 1] + ba[i][j - 1] + ba[i - 1][j] - ba[i - 1][j - 1]
num = int(input())
for _ in range(num):
    i, j, x, y = map(int, input().split())
    print(ba[x][y] - ba[x][j - 1] - ba[i - 1][y] + ba[i - 1][j - 1])
