import sys
input = sys.stdin.readline
print = sys.stdout.write

a = int(input())
lst = set()
sum = 0

for _ in range(a):
    chat = input().strip()
    if chat == "ENTER":
        sum += len(lst)
        lst.clear()
    else:
        lst.add(chat)

sum += len(lst)
print(f"{sum}\n") 