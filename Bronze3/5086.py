"""
문제
4 × 3 = 12이다.

이 식을 통해 다음과 같은 사실을 알 수 있다.

3은 12의 약수이고, 12는 3의 배수이다.

4도 12의 약수이고, 12는 4의 배수이다.

두 수가 주어졌을 때, 다음 3가지 중 어떤 관계인지 구하는 프로그램을 작성하시오.

첫 번째 숫자가 두 번째 숫자의 약수이다.
첫 번째 숫자가 두 번째 숫자의 배수이다.
첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다.
입력
입력은 여러 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 10,000이 넘지않는 두 자연수로 이루어져 있다. 마지막 줄에는 0이 2개 주어진다. 두 수가 같은 경우는 없다.

출력
각 테스트 케이스마다 첫 번째 숫자가 두 번째 숫자의 약수라면 factor를, 배수라면 multiple을, 둘 다 아니라면 neither를 출력한다.
"""
list=[]
while True:
    a,b = map(int, input().split())
    if a==0 and b==0:
        break
    else:
        list.append(a)
        list.append(b)
num = int(len(list)/2)
for i in range(1,num+1):
    if list[2*i-2]/list[2*i-1]>=1 and list[2*i-2]%list[2*i-1]==0:
        print("multiple")
    elif list[2*i-1]/list[2*i-2]>=1 and list[2*i-1]%list[2*i-2]==0:
        print("factor")
    else:
        print("neither")

