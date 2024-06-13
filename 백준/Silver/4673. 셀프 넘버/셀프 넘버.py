def self(n):
  stg = list(str(n))
  num = n
  for i in range(len(stg)):
    num+=int(stg[i])
  return num

lst = [i for i in range(1,10001)]
  
for i in range(1,10001):
  if self(i) in lst:
    lst.remove(self(i))

for i in range(len(lst)):
  print(lst[i])