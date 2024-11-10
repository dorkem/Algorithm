while 1:
   arr = list(map(int,input().split()))
   
   if arr[0] == 0:
      break

   arr.sort()
   if arr[2] >= arr[0]+arr[1]:
      print("Invalid")
   elif arr.count(arr[0]) == 3:
      print("Equilateral")
   elif arr.count(arr[0]) == 2 or arr.count(arr[1]) == 2:

      print("Isosceles")
   else:
      print("Scalene")