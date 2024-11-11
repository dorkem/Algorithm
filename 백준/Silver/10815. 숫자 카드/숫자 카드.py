n = int(input())
sang = list(map(int,input().split()))
k = int(input())
card = list(map(int,input().split()))

dict = {}

for i in card:
   dict[i] = 0

for i in sang:
   if i in dict:
      dict[i] = 1

for i in dict:
   print(dict[i], end=" ")