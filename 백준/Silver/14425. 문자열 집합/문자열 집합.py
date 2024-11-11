a, b = map(int,input().split())
arr = []
for i in range(a):
   word = input()
   arr.append(word)

sum = 0 
for i in range(b):
   n = input()
   if n in arr:
      sum += 1

print(sum)