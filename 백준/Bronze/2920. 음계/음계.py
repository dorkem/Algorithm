a = list(map(int, input().split()))
m = [
  [1,2,3,4,5,6,7,8],
  [8,7,6,5,4,3,2,1]
]
if a==m[0]:
  print("ascending")
elif a==m[1]:
  print("descending")
else:
  print("mixed")