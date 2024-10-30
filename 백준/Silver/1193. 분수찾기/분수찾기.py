n = int(input())
line = 1

while n > line:
    n -= line
    line += 1

if line % 2 == 0:
    son = n
    mom = line - n + 1
else:
    son = line - n + 1
    mom = n

print(f"{son}/{mom}")