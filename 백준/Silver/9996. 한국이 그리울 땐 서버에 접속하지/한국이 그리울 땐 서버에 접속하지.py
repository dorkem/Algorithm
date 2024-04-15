a= int(input())
pat = input().split("*")
l = len(pat[0]) + len(pat[1])

for i in range(a):
  word = input()
  if len(word)>=l and word.startswith(pat[0]) and word.endswith(pat[-1]):
    print("DA")
  else:
    print("NE")