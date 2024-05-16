from sys import stdin, stdout
input = stdin.readline 
print = stdout.write

student = []
for _ in range(int(input())):
    student.append(input().split())

student.sort(key = lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for i in student:
    print(i[0])
    print("\n")