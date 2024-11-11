from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
arr = deque([])
for i in range(n):
   m = input().split()
   
   if m[0] == '1':
      arr.appendleft(m[1])
   elif m[0] == '2':
      arr.append(m[1])
   elif m[0] == '3':
      if arr:
         print(arr.popleft())
      else:
         print("-1")
   elif m[0] == '4':
      if arr:
         print(arr.pop())
      else:
         print("-1")
   elif m[0] == '5':
      print(len(arr))
   elif m[0] == '6':
      if arr:
         print(0)
      else:
         print("1")
   elif m[0] == '7':
      if arr:
         print(arr[0])
      else:
         print("-1")
   else:
      if arr:
         print(arr[-1])
      else:
         print("-1")