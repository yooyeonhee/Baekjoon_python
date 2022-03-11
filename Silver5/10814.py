n = int(input())
j = []
for i in range(n):
    age, name = input().split()
    j.append(([int(age), name]))

j.sort(key=lambda a:int(a[0]))

for i in range(n):
    print(j[i][0], j[i][1])