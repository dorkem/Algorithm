def p(s):
  return s == s[::-1]

import sys
input = sys.stdin.readline
a = input().strip()

if all(char == a[0] for char in a):
    print(-1)
else:
    if not p(a):
        print(len(a))
    else:
        print(len(a) - 1)