t = int(input())
for tc in range(1,t+1):
   num = int(input())
   n = [2, 3, 5, 7, 11]
   arr = [0, 0, 0, 0, 0]

   while num != 1:
      for i in range(5):
         if num % n[i] == 0:
            arr[n.index(n[i])] += 1
            num //= n[i]
            break
   print(f"#{tc} {' '.join(map(str,arr))}")
