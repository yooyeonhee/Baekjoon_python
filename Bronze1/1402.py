"""
문제
어떤 정수 A가 있으면 그 숫자를 A = a1 * a2 * a3 * a4 ... * an으로 했을 때 A' = a1 + a2 + a3 ... + an이 성립하면 "A는 A'으로 변할 수 있다"라고 한다. (ai는 정수) 만약 A'이 A''으로 변할 수 있으면 "A는 A''으로 변할 수 있다"라고 한다.

이때 A와 B가 주어지면 A는 B로 변할 수 있는지 판별하시오.

입력
첫째 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 100)이 주어진다. 테스트 케이스마다 두 정수 A, B(-231 ≤ A, B ≤ 231-1)가 주어진다.

출력
각각의 테스트 케이스마다 한 줄에 변할 수 있으면 yes, 아니면 no를 출력한다.
"""
for _ in range(int(input())):
    A, B = map(int, input().split())
    print("yes")
