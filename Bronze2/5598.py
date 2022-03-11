"""
문제
가이우스 율리우스 카이사르(Gaius Julius Caesar)는 고대 로마 군인이자 정치가였습니다. 카이사르는 비밀스럽게 편지를 쓸 때, 'A'를 'D로', 'B'를 'E'로, 'C'를 'F'로... 이런 식으로 알파벳 문자를 3개씩 건너뛰어 적었다고 합니다.

26개의 대문자 알파벳으로 이루어진 단어를 카이사르 암호 형식으로 3문자를 옮겨 겹치지 않게 나열하여 얻은 카이사르 단어가 있습니다. 이 카이사르 단어를 원래 단어로 돌려놓는 프로그램을 작성하세요.

각 문자별로 변환 전과 변환 후를 나타낸 건 아래와 같습니다.

      변환전    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
      변환후    D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
예를 들어서, 이 방법대로 단어 'JOI'를 카이사르 단어 형식으로 변환한다면 'MRL'을 얻을 수 있고, 앞의 예와 같은 방법으로 얻은 카이사르 단어 'FURDWLD'를 원래 단어로 고치면 'CROATIA'가 됩니다.

입력
입력은 한 줄로 이루어져 있으며, 그 한 줄엔 대문자 알파벳으로 구성된 단어가 1개 있습니다.

입력받는 단어는 최대 1000자 이하입니다.

출력
출력은 입력받은 카이사르 단어를 원래 단어로 고친 걸 출력하시면 됩니다.
"""

word = input()
for i in range(0,len(word)):
    if word[i]=='A':
        print('X',end="")
    elif word[i]=='B':
        print("Y",end="")
    elif word[i] == 'C':
        print("Z", end="")
    else:
        print(chr(ord(word[i])-3),end="")