"""
문제
계란집을 운영하는 남욱이는 매일 닭장에서 달걀을 수거해간다. 어느 날 닭장에 들어가보니 일부 닭의 다리가 하나씩 사라졌다. 남욱이는 얼마나 많은 닭들이 한 다리를 잃었는지 알고싶었지만 닭이 너무 많아 셀 수 없었고, 대신 모든 닭의 다리수를 셌다. 고민하는 남욱이를 위해 모든 닭의 다리수의 합과 닭의 수를 가지고 이것을 해결해주자.

입력
첫째 줄에 총 테스트 케이스의 수 T (T ≤ 25)가, 둘째 줄 부터 T + 1째줄까지 매줄 마다 모든 닭의 다리수의 합 N (1 ≤ N ≤ 300)과 닭의 수 M (M ≤ N ≤ 2M)이 공백을 간격으로 입력된다.

출력
테스트 케이스마다 한줄에 다리가 잘린 닭의 수 U와 멀쩡한 닭의 수 T를 공백을 간격으로 출력한다.
"""
T = int(input())
for i in range(0,T):
    N, M = map(int, input().split())
    print(2*M-N, M-(2*M-N))