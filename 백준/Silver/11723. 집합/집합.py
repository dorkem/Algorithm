import sys
input = sys.stdin.readline

T = int(input())
arr = set()
for tc in range(T):
    M = input().strip().split()
    if M[0] == 'add':
        arr.add(M[1])
    elif M[0] == 'remove':
        arr.discard(M[1])
    elif M[0] == 'check':
        if M[1] in arr:
            print('1')
        else:
            print('0')
    elif M[0] == 'toggle':
        if M[1] in arr:
            arr.remove(M[1])
        else:
            arr.add(M[1])
    elif M[0] == 'all':
        arr = set(map(str, range(1, 21)))
    else:
        arr = set()
