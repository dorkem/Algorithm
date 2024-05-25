from collections import Counter
import sys

def modefinder(numbers):
    c = Counter(numbers)
    order = c.most_common()
    maximum = order[0][1]

    modes = []
    for num in order:
        if num[1] == maximum:
            modes.append(num[0])

    if len(modes) > 1:
        return sorted(modes)[1]
    else:
        return modes[0]
    
input = sys.stdin.read
data = input().split()
a = int(data[0])
lst = list(map(int, data[1:a+1]))
total = sum(lst)

print(round(total / a))
lst.sort()
print(lst[a // 2])
print(modefinder(lst))
print(lst[-1] - lst[0])
