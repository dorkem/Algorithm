a = int(input())
b = a
for i in range(a):
  word = input()
  for j in range(len(word)-1):
    if word[j] == word[j + 1]:
      pass
    elif word[j] in word[j + 1:]:
      b -= 1
      break
print(b)
