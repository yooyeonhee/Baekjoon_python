"""
문제
오늘은 NAVER D2 캠퍼스에서 CTP 스터디 하는날!!! 스터디 장소가 인하대학교 강의실에서 NAVER D2 캠퍼스로 바뀌었기 때문에 멀티탭 부장 준호는 스터디 전에 미리 멀티탭을 셋팅 해야 한다. CTP는 모든 사람이 사용할만큼 충분한 멀티탭을 가지고 있다. 종류는 3구부터 8구까지 다양하게 있다. 모든 사람들은 노트북만 가져오기 때문에 멀티탭 1구를 무조건 사용한다. 1구를 초과해선 안 된다.

CTP에는 멀티탭에 2개이상 연속으로 코드를 꽂으면 안되는 특별한 규칙이 있다. 준호는 미리 계산을 해서 모두가 코드를 꽂을 수 있게 멀티탭을 K개 챙겨 갔다.

하지만 준호는 수학과에서 수학을 못해 전과했기 때문에 가끔 멀티탭을 적게 가지고 올 때가 있다. 수학을 더 잘하는 여러분이 멀티탭을 충분히 챙겨왔는지 준호에게 알려주자



최초 전기 공급원(벽면 콘센트)는 총 K개이고, 각각의 멀티탭은 개별적으로 전기를 공급받는다. 즉, 멀티탭을 다른 멀티탭에 이어서 연결하는 경우는 없다.

입력
입력의 첫째 줄에 스터디에 온 학생의 수 N(1 ≤ N ≤ 100)명 멀티탭의 수 K(1 ≤ K ≤ 100)가 주어진다. 이후 두 번째 줄에 각 멀티탭 구의 수 A[i](3 ≤ A[i] ≤ 8) 가 주어진다.

출력
모든 사람이 멀티탭에 코드를 꽂을 수 있는경우 “YES” 아니라면 “NO”를 출력한다.
"""

N, K = map(int,input().split())
many = 0
multi = list(map(int,input().split()))
for i in range(0,K):
    if multi[i]%2==0:
        many = many+multi[i]//2
    elif multi[i]%2==1:
        many = many+multi[i]//2+1
if many<N:
    print("NO")
else:
    print("YES")
