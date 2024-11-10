arr = []
for i in range(3):
   angle = int(input())
   arr.append(angle)

if sum(arr) != 180:
   print("Error")
elif arr.count(60) == 3:
   print("Equilateral")
elif (arr.count(arr[0]) == 2 or arr.count(arr[1]) == 2) and sum(arr)==180:
   print("Isosceles")
else:
   print("Scalene")