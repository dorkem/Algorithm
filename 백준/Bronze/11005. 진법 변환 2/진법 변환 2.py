n, b = map(int, input().split())
alph = [chr(i) for i in range(ord('A'), ord('A') + (b - 10))]  # 필요한 만큼의 알파벳만 생성
arr = []

while n != 0:
    d = n % b
    n //= b
    if 10 <= d < b:
        arr.append(alph[d - 10])
    else:
        arr.append(str(d))

arr.reverse()
print("".join(arr))
