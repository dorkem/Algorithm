def spin(arr):
   arr1 = [[0]*n for _ in range(n)]
   for i in range(n):
      for j in range(n):
         arr1[i][j] = (arr[n-j-1][i])
   return arr1

   
t = int(input())
for tc in range(t):
   n = int(input())
   arr = [list(map(int, input().split())) for _ in range(n)]

   arr1 = spin(arr)
   arr2 = spin(arr1)
   arr3 = spin(arr2)

   print(f"#{tc+1}")
   for a, b, c in zip(arr1, arr2, arr3):
      print(f"{''.join(map(str,a))} {''.join(map(str,b))} {''.join(map(str,c))}") 