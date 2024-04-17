start = int(input())
last = int(input())

list = []
for num in range(start, last+1):
    h = 0
    if num > 1 :
        for i in range(2, num):
            if num % i == 0:
              h += 1
              break
        if h == 0:
            list.append(num)

if len(list) > 0 :
  print(sum(list))
  print(min(list))
else:
  print(-1)