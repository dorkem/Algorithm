a = input()
result = []
for i in a:
  if 'a' <= i <= 'z':
    b = (((ord(i)-ord('a'))+13)%26)+ord('a')
    result.append(chr(b))
  elif 'A' <= i <= 'Z':
    b = (((ord(i)-ord('A'))+13)%26)+ord('A')
    result.append(chr(b))
  else :
    result.append(i)

print(''.join(result))