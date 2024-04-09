a = input()
al = [0]*26
for i in a:
  al[ord(i)-97] += 1
print(*al)