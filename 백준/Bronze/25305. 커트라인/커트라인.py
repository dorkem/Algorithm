import sys
input = sys.stdin.readline
a, b = map(int,input().split())
list = list(map(int,input().split()))
list.sort()
print(list[-b])