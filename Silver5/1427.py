num = int(input())
list=[]
for i in str(num):
    list.append(i)

list.sort()
list.reverse()
for j in list:
    print(j, end="")