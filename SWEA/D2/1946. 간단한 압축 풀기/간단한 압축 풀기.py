t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = []
    word = ""
    for i in range(n):
        c, k = map(str, input().split())
        k = int(k)
        word += c * k
    print(f"#{tc}")
    
    for i in range(len(word)//10+1):
        print(word[i*10:i*10+10])