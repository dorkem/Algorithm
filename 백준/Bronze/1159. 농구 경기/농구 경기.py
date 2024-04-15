al = [0]*26
a = int(input())
for _ in range(a):
  name = input()
  al[ord(name[0])-97] += 1

predaja = True
for i in range(26):
  if al[i] >= 5:
    print(chr(i + 97), end='')
    predaja = False

if predaja:
  print("PREDAJA")