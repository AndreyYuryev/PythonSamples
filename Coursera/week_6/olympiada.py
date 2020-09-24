grade = list()
n = int(input())
for i in range(n):
    grade.append(input().split())
grade.sort(key=lambda grade: -int(grade[1]))
for now in grade:
    print(now[0])
