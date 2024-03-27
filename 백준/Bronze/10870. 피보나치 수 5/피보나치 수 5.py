num = int(input())
a, b = 0, 1
if num == 0 or num == 1:
    print(num)
else:
  for i in range(2, num + 1):
    a, b = b, a + b
  print(b)