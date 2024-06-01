a = int(input())
word = input()
sum = 0
mod = 1234567891
for i in range(len(word)):
  b = ord(word[i]) - 96
  sum += b * (31**i)
print(sum % mod)